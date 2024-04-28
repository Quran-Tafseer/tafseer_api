package tafseer_api

import (
	"context"
	"github.com/labstack/echo/v4"
	"net/http"
	"os"
	"os/signal"
	"tafseer_api/config"
	"tafseer_api/data"
	"tafseer_api/router"
	"time"
)

func Run() error {
	echoSvc := echo.New()

	// Load configuration using yaml file
	cfg, err := config.LoadConfig()
	if err != nil {
		return err
	}

	// Setup logger
	logger := cfg.ConfigLogger()

	// Echo middlewares
	config.SetupMiddlewares(echoSvc, logger)

	// Setup database
	db := cfg.Database.ConnectDB()

	// Setup routes
	// Setup Quran Endpoints
	quranDBRepo := data.NewQuranRepository(db)
	router.SetupQuranRouterNServices(echoSvc, quranDBRepo)

	// Setup Tafseer Endpoints
	tafseerDBRepo := data.NewTafseerRepository(db)
	router.SetupTafseerRouterServices(echoSvc, tafseerDBRepo)

	// Start server
	go func() {
		if err = echoSvc.Start(cfg.FullAddress()); err != nil && err != http.ErrServerClosed {
			echoSvc.Logger.Fatal("shutting down the server")
		}
	}()

	// Wait for interrupt signal to gracefully shutdown the server with a timeout of 10 seconds.
	// Use a buffered channel to avoid missing signals as recommended for signal.Notify
	quit := make(chan os.Signal, 1)
	signal.Notify(quit, os.Interrupt)
	<-quit
	ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
	defer cancel()
	if err := echoSvc.Shutdown(ctx); err != nil {
		echoSvc.Logger.Fatal(err)
	}
	return nil

}
