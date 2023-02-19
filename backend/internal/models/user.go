package models

import (
	"backend/internal/db"
	"time"

	"golang.org/x/crypto/bcrypt"
)

type User struct {
	Id        string    `json:"id" gorm:"primaryKey"`
	Username  string    `json:"username"`
	Password  string    `json:"-"`
	CreatedAt time.Time `json:"created_at"`
	UpdatedAt time.Time `json:"updated_at"`
}

func HashPassword(password string) (string, error) {
	bytes, err := bcrypt.GenerateFromPassword([]byte(password), 14)
	return string(bytes), err
}

func (u *User) CheckPasswordHash(attempt string) bool {
	err := bcrypt.CompareHashAndPassword([]byte(u.Password), []byte(attempt))
	return err == nil
}

func (u *User) Save() error {
	u.UpdatedAt = time.Now()
	return db.DB.Save(u).Error
}

func GetUserByID(id string) (*User, error) {
	user := &User{
		Id: id,
	}

	err := db.DB.Find(user).Error
	if err != nil {
		return nil, err
	}
	return user, nil
}

func GetUserByUsername(username string) (*User, error) {
	user := &User{
		Username: username,
	}

	err := db.DB.Find(user).Error

	if err != nil {
		return nil, err
	}
	return user, nil
}
