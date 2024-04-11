package service

import (
	"github.com/labstack/echo/v4"
	"github.com/stretchr/testify/assert"
	"net/http/httptest"
	"tafseer_api/domain"
	"testing"
)

type TafseerDomainMock struct {
	TafseerList  *domain.TafseerListDetailsResponse
	Tafseer      *domain.AyahTafseerResponse
	TafseerRange *domain.AyahTafseerListResponse
	Err          error
}

func (m *TafseerDomainMock) GetTafseerList() (*domain.TafseerListDetailsResponse, error) {
	return m.TafseerList, m.Err
}

func (m *TafseerDomainMock) GetAyahTafseer(surahIndex, ayahNumber, tafseerId string) (*domain.AyahTafseerResponse, error) {
	// Mimic the behavior of passing an invalid tafseerId (404)
	if tafseerId != "1" {
		return nil, nil
	}

	return m.Tafseer, m.Err
}

func (m *TafseerDomainMock) GetAyahRangeTafseer(surahIndex, ayahNumberFrom, ayahNumberTo, tafseerId string) (*domain.AyahTafseerListResponse, error) {
	// Mimic the behavior of passing an invalid tafseerId (404)
	if tafseerId != "1" {
		return nil, nil
	}

	return m.TafseerRange, m.Err
}

func TestTafseerService_GetTafseerList(t *testing.T) {
	tafseerDomainMock := &TafseerDomainMock{
		TafseerList: &domain.TafseerListDetailsResponse{
			domain.TafseerDetails{
				Id:       1,
				Name:     "Tafseer Ibn Kathir",
				Author:   "Ibn Kathir",
				BookName: "Tafseer Ibn Kathir",
				Language: "Arabic",
			},
		},
		Err: nil,
	}
	tafseerService := NewTafseerService(tafseerDomainMock)

	e := echo.New()
	req := httptest.NewRequest(echo.GET, "/tafseer", nil)
	rec := httptest.NewRecorder()
	c := e.NewContext(req, rec)

	err := tafseerService.GetTafseerList(c)
	assert.NoError(t, err)
	assert.Equal(t, 200, rec.Code)
}

func TestTafseerService_GetAyahTafseer(t *testing.T) {
	tafseerDomainMock := &TafseerDomainMock{
		Tafseer: &domain.AyahTafseerResponse{
			TafseerId:   1,
			TafseerName: "Tafseer Ibn Kathir",
			AyahUrl:     "http://localhost:8080/tafseer/1/1/1",
			AyahNumber:  1,
			Text:        "This is the tafseer of the ayah",
		},
		Err: nil,
	}
	tafseerService := NewTafseerService(tafseerDomainMock)

	e := echo.New()
	req := httptest.NewRequest(echo.GET, "/tafseer/1/1/1", nil)
	rec := httptest.NewRecorder()
	c := e.NewContext(req, rec)
	c.SetParamNames("surah_index", "ayah_number", "tafseer_id")
	c.SetParamValues("1", "1", "1")

	err := tafseerService.GetAyahTafseer(c)
	assert.NoError(t, err)
	assert.Equal(t, 200, rec.Code)
}

func TestTafseerService_GetAyahTafseer_NotFound(t *testing.T) {
	tafseerDomainMock := &TafseerDomainMock{
		Tafseer: &domain.AyahTafseerResponse{},
		Err:     nil,
	}
	tafseerService := NewTafseerService(tafseerDomainMock)

	e := echo.New()
	req := httptest.NewRequest(echo.GET, "/tafseer/2/1/1", nil)
	rec := httptest.NewRecorder()
	c := e.NewContext(req, rec)
	c.SetParamNames("surah_index", "ayah_number", "tafseer_id")
	c.SetParamValues("1", "1", "2")

	err := tafseerService.GetAyahTafseer(c)
	assert.NoError(t, err)
	assert.Equal(t, 404, rec.Code)
}

func TestTafseerService_GetAyahRangeTafseer(t *testing.T) {
	tafseerDomainMock := &TafseerDomainMock{
		TafseerRange: &domain.AyahTafseerListResponse{
			domain.AyahTafseerResponse{
				TafseerId:   1,
				TafseerName: "Tafseer Ibn Kathir",
				AyahUrl:     "http://localhost:8080/tafseer/1/1/1",
				AyahNumber:  1,
				Text:        "This is the tafseer of the ayah",
			},
			domain.AyahTafseerResponse{
				TafseerId:   1,
				TafseerName: "Tafseer Ibn Kathir",
				AyahUrl:     "http://localhost:8080/tafseer/1/1/2",
				AyahNumber:  2,
				Text:        "This is the tafseer of the ayah",
			},
		},
		Err: nil,
	}
	tafseerService := NewTafseerService(tafseerDomainMock)

	e := echo.New()
	req := httptest.NewRequest(echo.GET, "/tafseer/1/2/1/1", nil)
	rec := httptest.NewRecorder()
	c := e.NewContext(req, rec)
	c.SetParamNames("surah_index", "ayah_from", "ayah_to", "tafseer_id")
	c.SetParamValues("1", "1", "2", "1")

	err := tafseerService.GetAyahRangeTafseer(c)
	assert.NoError(t, err)
	assert.Equal(t, 200, rec.Code)
}

func TestTafseerService_GetAyahRangeTafseer_NotFound(t *testing.T) {
	tafseerDomainMock := &TafseerDomainMock{
		TafseerRange: &domain.AyahTafseerListResponse{},
		Err:          nil,
	}
	tafseerService := NewTafseerService(tafseerDomainMock)

	e := echo.New()
	req := httptest.NewRequest(echo.GET, "/tafseer/2/1/1/2", nil)
	rec := httptest.NewRecorder()
	c := e.NewContext(req, rec)
	c.SetParamNames("surah_index", "ayah_from", "ayah_to", "tafseer_id")
	c.SetParamValues("1", "1", "2", "2")

	err := tafseerService.GetAyahRangeTafseer(c)
	assert.NoError(t, err)
	assert.Equal(t, 404, rec.Code)
}
