package domain

import "tafseer_api/data"

type TafseerDomain struct {
	repo *data.TafseerRepository
}

func NewTafseerDomain(repo *data.TafseerRepository) *TafseerDomain {
	return &TafseerDomain{repo: repo}
}

func (d *TafseerDomain) GetTafseerList() (*TafseerListDetailsResponse, error) {
	tafseerList, err := (*d.repo).GetTafseerList()
	if err != nil {
		return nil, err
	}

	var details TafseerListDetailsResponse

	for _, t := range tafseerList {
		detail := TafseerDetails{
			Id:       t.Id,
			Name:     t.Name,
			Author:   t.Author,
			BookName: t.BookName,
			Language: t.Language,
		}
		details = append(details, detail)
	}

	return &details, nil
}

func (d *TafseerDomain) GetAyahTafseer(surahIndex string, ayahNumber string, tafseerId string) (*AyahTafseerResponse, error) {
	tafseer, err := (*d.repo).GetAyahTafseer(surahIndex, ayahNumber, tafseerId)
	if err != nil {
		return nil, err
	}

	if tafseer == nil {
		return nil, nil
	}

	detail := AyahTafseerResponseFromTafseer(tafseer)

	return detail, nil
}

func (d *TafseerDomain) GetAyahRangeTafseer(surahIndex string, ayahNumberFrom string, ayahNumberTo string, tafseerId string) (*AyahTafseerListResponse, error) {
	tafseerRange, err := (*d.repo).GetAyahRangeTafseer(surahIndex, ayahNumberFrom, ayahNumberTo, tafseerId)
	if err != nil {
		return nil, err
	}

	if tafseerRange == nil {
		return nil, nil
	}

	var tafseer AyahTafseerListResponse

	for _, t := range tafseerRange {
		detail := AyahTafseerResponse{
			TafseerId:   t.Id,
			TafseerName: t.Tafseer.Name,
			AyahUrl:     t.GetAyahUrl(),
			AyahNumber:  t.Ayah.Number,
			Text:        t.Text,
		}
		tafseer = append(tafseer, detail)
	}

	return &tafseer, nil
}
