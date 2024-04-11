package service

import (
	"github.com/labstack/echo/v4"
	"tafseer_api/domain"
)

type QuranService struct {
	svc domain.QuranDomainer
}

func NewQuranService(svc domain.QuranDomainer) *QuranService {
	return &QuranService{svc: svc}
}

func (s *QuranService) GetSurahs(c echo.Context) error {
	// Get surahs from database
	surahs, err := s.svc.GetSurahs()
	if err != nil {
		return err
	}

	if surahs == nil {
		return c.JSON(404, "No surahs found")
	}

	return c.JSON(200, surahs)
}

func (s QuranService) GetAyah(c echo.Context) error {
	surahIndex := c.Param("sura_number")
	ayahNumber := c.Param("ayah_number")
	ayah, err := s.svc.GetAyah(surahIndex, ayahNumber)
	if err != nil {
		return err
	}

	if ayah == nil {
		return c.JSON(404, "No ayah found")
	}

	return c.JSON(200, ayah)
}
