package config

import (
	"github.com/kkyr/fig"
	"go.uber.org/zap"
)

type Config struct {
	Service
	Logger zap.Logger
	Database
}

func LoadConfig() (*Config, error) {
	var cfg Config

	if err := fig.Load(&cfg, fig.File("config.yaml"), fig.UseEnv("svc")); err != nil {
		return nil, err
	}

	return &cfg, nil
}
