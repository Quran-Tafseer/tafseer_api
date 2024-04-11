package service

import (
	"github.com/labstack/echo/v4"
	"github.com/stretchr/testify/assert"
	"net/http/httptest"
	"tafseer_api/domain"
	"testing"
)

type QuranDomainMock struct {
	Surahs *domain.SurahListResponse
	Ayah   *domain.AyahDetailsResponse
	Err    error
}

var _ domain.QuranDomainer = &QuranDomainMock{}

func (m *QuranDomainMock) GetSurahs() (*domain.SurahListResponse, error) {
	return m.Surahs, m.Err
}

func (m *QuranDomainMock) GetAyah(surahIndex, ayahNumber string) (*domain.AyahDetailsResponse, error) {
	// Mimic the behavior of the real GetAyah method where the ayah is not found (404)
	if surahIndex != "1" || ayahNumber != "1" {
		return nil, nil
	}

	return m.Ayah, m.Err
}

func TestQuranService_GetSurahs(t *testing.T) {
	surahs := domain.SurahListResponse{
		domain.SurahResponse{
			Index: 1,
			Name:  "Al-Fatihah",
		},
		domain.SurahResponse{
			Index: 2,
			Name:  "Al-Baqarah",
		},
	}
	quranDomainMock := &QuranDomainMock{
		Surahs: &surahs,
		Err:    nil,
	}
	quranService := NewQuranService(quranDomainMock)

	e := echo.New()
	req := httptest.NewRequest(echo.GET, "/surahs", nil)
	rec := httptest.NewRecorder()
	c := e.NewContext(req, rec)

	err := quranService.GetSurahs(c)
	assert.NoError(t, err)
	assert.Equal(t, 200, rec.Code)

}

func TestQuranService_GetAyah(t *testing.T) {
	quranDomainMock := &QuranDomainMock{
		Ayah: &domain.AyahDetailsResponse{
			SuraIndex:  1,
			AyahNumber: 1,
			SuraName:   "Al-Fatihah",
			Text:       "In the name of Allah, the Entirely Merciful, the Especially Merciful.",
		},
		Err: nil,
	}
	quranService := NewQuranService(quranDomainMock)

	e := echo.New()
	req := httptest.NewRequest(echo.GET, "/surahs/1/ayahs/1", nil)
	rec := httptest.NewRecorder()
	c := e.NewContext(req, rec)
	c.SetParamNames("sura_number", "ayah_number")
	c.SetParamValues("1", "1")

	err := quranService.GetAyah(c)
	assert.NoError(t, err)
	assert.Equal(t, 200, rec.Code)
}

func TestQuranService_GetAyah_NotFound(t *testing.T) {
	quranDomainMock := &QuranDomainMock{
		Ayah: &domain.AyahDetailsResponse{
			SuraIndex:  1,
			AyahNumber: 1,
			SuraName:   "Al-Fatihah",
			Text:       "In the name of Allah, the Entirely Merciful, the Especially Merciful.",
		},
		Err: nil,
	}
	quranService := NewQuranService(quranDomainMock)

	e := echo.New()
	req := httptest.NewRequest(echo.GET, "/surahs/1/ayahs/1", nil)
	rec := httptest.NewRecorder()
	c := e.NewContext(req, rec)
	c.SetParamNames("sura_number", "ayah_number")
	c.SetParamValues("2", "2")

	err := quranService.GetAyah(c)
	assert.NoError(t, err)
	assert.Equal(t, 404, rec.Code)
}
