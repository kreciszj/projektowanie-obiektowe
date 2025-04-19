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

	// dane z API
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

	port := os.Getenv("PORT")
	if port == "" {
		port = "8080"
	}
	e.Logger.Fatal(e.Start(":" + port))
}
