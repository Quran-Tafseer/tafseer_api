package config

import "go.uber.org/zap"

func NewLogger(env string) *zap.Logger {
	switch env {
	case "dev":
		logger, _ := zap.NewDevelopment()
		return logger
	case "prod":
		logger, _ := zap.NewProduction()
		return logger
	default:
		logger, _ := zap.NewDevelopment()
		return logger
	}
}
