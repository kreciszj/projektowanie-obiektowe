package main

import (
	"encoding/json"
	"log"
	"net/http"
	"os"
	"strconv"

	"github.com/labstack/echo/v4"
	"zadanie4/internal/db"
	"zadanie4/internal/proxy"
	"zadanie4/internal/weather"
)

func main() {
	database, err := db.New()
	if err != nil {
		log.Fatal(err)
	}
	if err := database.AutoMigrate(&weather.Weather{}); err != nil {
		log.Fatal(err)
	}
	if err := weather.Seed(database); err != nil {
		log.Fatal(err)
	}

	e := echo.New()
	p := proxy.NewOpenMeteoProxy()

	// dane z bazy
	e.GET("/weather/db", func(c echo.Context) error {
		var records []weather.Weather
		if err := database.Find(&records).Error; err != nil {
			return c.String(http.StatusInternalServerError, "db error")
		}
		return c.JSONPretty(http.StatusOK, records, "  ")
	})

	// dane z API - pojedyncze
	e.GET("/weather/live", func(c echo.Context) error {
		latStr := c.QueryParam("lat")
		lonStr := c.QueryParam("lon")
		if latStr == "" || lonStr == "" {
			return c.String(http.StatusBadRequest, "missing lat or lon query param")
		}
	
		raw, err := p.Fetch(latStr, lonStr)
		if err != nil {
			log.Println(err)
			return c.String(http.StatusBadGateway, "external fetch failed")
		}
	
		type omResp struct {
			CurrentWeather struct {
				Temperature float64 `json:"temperature"`
			} `json:"current_weather"`
		}
		var om omResp
		if err := json.Unmarshal(raw, &om); err != nil {
			return c.String(http.StatusBadGateway, "invalid external response")
		}
	
		latF, _ := strconv.ParseFloat(latStr, 64)
		lonF, _ := strconv.ParseFloat(lonStr, 64)
	
		rec := weather.Weather{
			Location:  latStr + "," + lonStr,
			Latitude:  latF,
			Longitude: lonF,
			TempC:     om.CurrentWeather.Temperature,
		}
		if err := database.Create(&rec).Error; err != nil {
			log.Println(err)
			return c.String(http.StatusInternalServerError, "db write error")
		}
	
		return c.JSONPretty(http.StatusOK, rec, "  ")
	})

	type locationReq struct {
		Lat float64 `json:"lat"`
		Lon float64 `json:"lon"`
	}
	
	// dane z API - wiele na raz
	e.POST("/weather/live/list", func(c echo.Context) error {
		var req []locationReq
		if err := c.Bind(&req); err != nil {
			return c.String(http.StatusBadRequest, "invalid json")
		}
		if len(req) == 0 {
			return c.String(http.StatusBadRequest, "empty list")
		}
	
		type omResp struct {
			CurrentWeather struct {
				Temperature float64 `json:"temperature"`
			} `json:"current_weather"`
		}
	
		results := make([]weather.Weather, 0, len(req))
		for _, loc := range req {
			latStr := strconv.FormatFloat(loc.Lat, 'f', 6, 64)
			lonStr := strconv.FormatFloat(loc.Lon, 'f', 6, 64)
	
			raw, err := p.Fetch(latStr, lonStr)
			if err != nil {
				log.Println(err)
				continue
			}
			var om omResp
			if err := json.Unmarshal(raw, &om); err != nil {
				log.Println(err)
				continue
			}
			rec := weather.Weather{
				Location:  latStr + "," + lonStr,
				Latitude:  loc.Lat,
				Longitude: loc.Lon,
				TempC:     om.CurrentWeather.Temperature,
			}
			if err := database.Create(&rec).Error; err != nil {
				log.Println(err)
				continue
			}
			results = append(results, rec)
		}
	
		return c.JSONPretty(http.StatusOK, results, "  ")
	})	

	port := os.Getenv("PORT")
	if port == "" {
		port = "8080"
	}
	e.Logger.Fatal(e.Start(":" + port))
}
