package weather

import "gorm.io/gorm"

var seedData = []Weather{
	{Location: "Warsaw", TempC: 17.4},
	{Location: "Krakow", TempC: 16.2},
	{Location: "Gdansk", TempC: 14.9},
}

func Seed(db *gorm.DB) error {
	for _, w := range seedData {
		if err := db.Create(&w).Error; err != nil {
			return err
		}
	}
	return nil
}
