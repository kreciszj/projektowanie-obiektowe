package db

import (
	"gorm.io/driver/sqlite"
	"gorm.io/gorm"
)

func New() (*gorm.DB, error) {
	return gorm.Open(sqlite.Open("weather.db"), &gorm.Config{})
}
