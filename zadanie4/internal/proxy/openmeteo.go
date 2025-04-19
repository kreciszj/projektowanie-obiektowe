package proxy

import (
	"io"
	"net/http"
)

type WeatherProxy interface {
	Fetch(lat, lon string) ([]byte, error)
}

type OpenMeteoProxy struct {
	client *http.Client
}

func NewOpenMeteoProxy() *OpenMeteoProxy {
	return &OpenMeteoProxy{client: &http.Client{}}
}

func (p *OpenMeteoProxy) Fetch(lat, lon string) ([]byte, error) {
	req, err := http.NewRequest(http.MethodGet, "https://api.open-meteo.com/v1/forecast", nil)
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
