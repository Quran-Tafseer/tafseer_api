package config

import (
	"github.com/ilyakaznacheev/cleanenv"
	"go.uber.org/zap"
)

type Config struct {
	Service
	Logger   zap.Logger
	LogLevel string `yaml:"log_level" env:"LOG_LEVEL" env-default:"info"`
	Database
}

func LoadConfig() (*Config, error) {
	var cfg Config

	if err := cleanenv.ReadEnv(&cfg); err != nil {
		return nil, err
	}

	return &cfg, nil
}

func (c Config) ConfigLogger() *zap.Logger {
	return NewLogger(c.Env, c.LogLevel)
}
