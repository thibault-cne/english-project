package models

import "backend/internal/db"

func Migrate() {
	db.DB.AutoMigrate(&User{})
}
