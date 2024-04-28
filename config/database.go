package config

import (
	"fmt"
	"gorm.io/driver/postgres"
	"gorm.io/gorm"
)

type Database struct {
	Host     string `yaml:"host" env:"DB_HOST" env-default:"localhost"`
	Port     string `yaml:"port" env:"DB_PORT" env-default:"3306"`
	User     string `yaml:"user" env:"DB_USER" env-default:"root"`
	Password string `yaml:"password" env:"DB_PASS" env-default:""`
	DBName   string `yaml:"dbname" env:"DB_NAME" env-default:"golang_rest_service_template"`
	SSLMode  string `yaml:"sslmode" env:"DB_SSL_MODE" env-default:"disable"`
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
