package domain

import "tafseer_api/data"

type QuranDomain struct {
	repo *data.QuranRepository
}

func NewQuranDomain(repo *data.QuranRepository) *QuranDomain {
	return &QuranDomain{repo: repo}
}

func (d *QuranDomain) GetSurahs() (*SurahListResponse, error) {
	surahs, err := (*d.repo).GetSuras()
	if err != nil {
		return nil, err
	}

	surahsRes := SurahListResponseFromSurahs(surahs)

	return surahsRes, nil
}

func (d *QuranDomain) GetAyah(surahIndex, ayahNumber string) (*AyahDetailsResponse, error) {
	ayah, err := (*d.repo).GetAyah(surahIndex, ayahNumber)
	if err != nil {
		return nil, err
	}

	if ayah == nil {
		return nil, nil
	}

	ayahRes := AyahDetailsResponseFromAyah(ayah)

	return ayahRes, nil
}
