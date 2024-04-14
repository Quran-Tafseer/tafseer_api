package config

import (
	"github.com/labstack/echo/v4"
	"github.com/labstack/echo/v4/middleware"
	"github.com/labstack/gommon/log"
	"go.uber.org/zap"
)

func setupLoggerMiddleware(echoSvc *echo.Echo, logger *zap.Logger) {
	echoSvc.Use(middleware.RequestLoggerWithConfig(middleware.RequestLoggerConfig{
		LogURI:    true,
		LogStatus: true,
		LogValuesFunc: func(c echo.Context, v middleware.RequestLoggerValues) error {
			logger.Info("request",
				zap.String("URI", v.URI),
				zap.Int("status", v.Status),
			)

			return nil
		},
	}))
}

func setupWebMiddleware(echoSvc *echo.Echo) {
	echoSvc.Use(middleware.GzipWithConfig(middleware.GzipConfig{
		Level: 5,
	}))
	echoSvc.Use(middleware.RecoverWithConfig(middleware.RecoverConfig{
		StackSize: 4 << 10, // 4 KB
		LogLevel:  log.ERROR,
	}))
}

func SetupMiddlewares(echoSvc *echo.Echo, logger *zap.Logger) {
	setupLoggerMiddleware(echoSvc, logger)
	setupWebMiddleware(echoSvc)
}
