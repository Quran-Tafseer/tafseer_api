package config

import (
	"fmt"
	"gorm.io/driver/postgres"
	"gorm.io/gorm"
)

type Database struct {
	Host     string `fig:"host" default:"localhost"`
	Port     string `fig:"port" default:"3306"`
	User     string `fig:"user" default:"root"`
	Password string `fig:"password" default:""`
	DBName   string `fig:"dbname" default:"golang_rest_service_template"`
	SSLMode  string `fig:"sslmode" default:"disable"`
}

func (db *Database) GetDSN() string {
	//"host=localhost user=gorm password=gorm dbname=gorm port=9920 sslmode=disable TimeZone=UTC"
	return fmt.Sprintf("host=%s user=%s password=%s dbname=%s port=%s sslmode=%s TimeZone=UTC", db.Host, db.User, db.Password, db.DBName, db.Port, db.SSLMode)
}

// Configure the gorm database connection

func (db *Database) ConnectDB() *gorm.DB {
	dbConn, err := gorm.Open(postgres.Open(db.GetDSN()), &gorm.Config{})
	if err != nil {
		panic("Failed to connect to database!")
	}
	return dbConn
}
