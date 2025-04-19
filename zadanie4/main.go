package main

import (
	"log"
	"net/http"
	"os"

	"github.com/labstack/echo/v4"
	"zadanie4/internal/db"
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

	e.GET("/weather", func(c echo.Context) error {
		var records []weather.Weather
		if err := database.Find(&records).Error; err != nil {
			return c.String(http.StatusInternalServerError, "db error")
		}
		return c.JSONPretty(http.StatusOK, records, "  ")
	})

	port := os.Getenv("PORT")
	if port == "" {
		port = "8080"
	}
	e.Logger.Fatal(e.Start(":" + port))
}
