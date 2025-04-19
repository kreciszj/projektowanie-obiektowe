package weather

import "time"

type Weather struct {
	ID        uint      `gorm:"primaryKey"`
	Location  string
	Latitude  float64
	Longitude float64
	TempC     float64
	CreatedAt time.Time
}
