package main

import (
	"encoding/json"
	"io"
	"log"
	"net/http"
	"os"

	"github.com/labstack/echo/v4"
)

type weatherProxy struct {
	client *http.Client
}

func newWeatherProxy() *weatherProxy {
	return &weatherProxy{client: &http.Client{}}
}

func (p *weatherProxy) fetch(lat, lon string) ([]byte, error) {
	req, err := http.NewRequest(
		http.MethodGet,
		"https://api.open-meteo.com/v1/forecast",
		nil,
	)
	if err != nil {
		return nil, err
	}
	q := req.URL.Query()
	q.Set("latitude", lat)
	q.Set("longitude", lon)
	q.Set("current_weather", "true")
	req.URL.RawQuery = q.Encode()

	resp, err := p.client.Do(req)
	if err != nil {
		return nil, err
	}
	defer resp.Body.Close()

	return io.ReadAll(resp.Body)
}

func main() {
	e := echo.New()
	p := newWeatherProxy()

	e.GET("/weather", func(c echo.Context) error {
		lat := c.QueryParam("lat")
		lon := c.QueryParam("lon")
		if lat == "" || lon == "" {
			return c.String(http.StatusBadRequest, "missing lat or lon query param")
		}

		data, err := p.fetch(lat, lon)
		if err != nil {
			log.Println(err)
			return c.String(http.StatusBadGateway, "failed to fetch external data")
		}

		var trimmed map[string]any
		if err := json.Unmarshal(data, &trimmed); err != nil {
			return c.String(http.StatusBadGateway, "invalid external response")
		}

		return c.JSONPretty(http.StatusOK, trimmed, "  ")
	})

	port := os.Getenv("PORT")
	if port == "" {
		port = "8080"
	}
	e.Logger.Fatal(e.Start(":" + port))
}
