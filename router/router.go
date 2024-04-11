package router

import (
	"github.com/labstack/echo/v4"
	"tafseer_api/data"
	"tafseer_api/domain"
	"tafseer_api/service"
)

func SetupQuranRouterNServices(e *echo.Echo, db data.QuranRepository) {
	quranDomain := domain.NewQuranDomain(&db)
	quranSvc := service.NewQuranService(quranDomain)
	e.GET("/quran", quranSvc.GetSurahs)
	e.GET("/quran/:sura_number/:ayah_number", quranSvc.GetAyah)
}

func SetupTafseerRouterServices(e *echo.Echo, db data.TafseerRepository) {
	tafseerDomain := domain.NewTafseerDomain(&db)
	tafseerSvc := service.NewTafseerService(tafseerDomain)
	e.GET("/tafseer", tafseerSvc.GetTafseerList)
	e.GET("/tafseer/:tafseer_id/:surah_index/:ayah_number", tafseerSvc.GetAyahTafseer)
	e.GET("/tafseer/:tafseer_id/:surah_index/:ayah_from/:ayah_to", tafseerSvc.GetAyahRangeTafseer)
}
