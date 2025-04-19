package weather

import "time"

type Weather struct {
	ID        uint      `gorm:"primaryKey"`
	Location  string
	TempC     float64
	CreatedAt time.Time
}
