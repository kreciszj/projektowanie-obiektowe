package main

import (
	"encoding/json"
	"log"
	"net/http"
	"os"

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
		lat := c.QueryParam("lat")
		lon := c.QueryParam("lon")
		if lat == "" || lon == "" {
			return c.String(http.StatusBadRequest, "missing lat or lon query param")
		}

		raw, err := p.Fetch(lat, lon)
		if err != nil {
			log.Println(err)
			return c.String(http.StatusBadGateway, "external fetch failed")
		}

		var out map[string]any
		if err := json.Unmarshal(raw, &out); err != nil {
			return c.String(http.StatusBadGateway, "invalid external response")
		}
		return c.JSONPretty(http.StatusOK, out, "  ")
	})

	port := os.Getenv("PORT")
	if port == "" {
		port = "8080"
	}
	e.Logger.Fatal(e.Start(":" + port))
}
