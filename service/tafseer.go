package service

import (
	"github.com/labstack/echo/v4"
	"tafseer_api/domain"
)

type TafseerService struct {
	svc *domain.TafseerDomain
}

func NewTafseerService(svc *domain.TafseerDomain) *TafseerService {
	return &TafseerService{svc: svc}
}

func (s *TafseerService) GetTafseerList(c echo.Context) error {
	tafseerList, err := (*s.svc).GetTafseerList()
	if err != nil {
		return err
	}

	if tafseerList == nil {
		return c.JSON(404, "No tafseer found")
	}

	return c.JSON(200, tafseerList)
}

func (s *TafseerService) GetAyahTafseer(c echo.Context) error {
	surahIndex := c.Param("surah_index")
	ayahNumber := c.Param("ayah_number")
	tafseerId := c.Param("tafseer_id")
	tafseer, err := (*s.svc).GetAyahTafseer(surahIndex, ayahNumber, tafseerId)
	if err != nil {
		return err
	}

	if tafseer == nil {
		return c.JSON(404, "No tafseer found")
	}

	return c.JSON(200, tafseer)
}

func (s *TafseerService) GetAyahRangeTafseer(c echo.Context) error {
	// Get tafseer for a single ayah from database
	surahIndex := c.Param("surah_index")
	ayahNumberFrom := c.Param("ayah_from")
	ayahNumberTo := c.Param("ayah_to")
	tafseerId := c.Param("tafseer_id")

	tafseerRange, err := (*s.svc).GetAyahRangeTafseer(surahIndex, ayahNumberFrom, ayahNumberTo, tafseerId)
	if err != nil {
		return err
	}

	if tafseerRange == nil {
		return c.JSON(404, "No tafseer found")
	}

	return c.JSON(200, tafseerRange)
}
