package domain

import "tafseer_api/data"

type SurahResponse struct {
	Index int    `json:"index"`
	Name  string `json:"name"`
}

type SurahListResponse []SurahResponse

func SurahListResponseFromSurahs(s []data.Sura) *SurahListResponse {
	var chapters SurahListResponse

	for _, surah := range s {
		chapter := SurahResponse{
			Index: surah.Index,
			Name:  surah.Name,
		}
		chapters = append(chapters, chapter)
	}
	return &chapters
}

type AyahDetailsResponse struct {
	SuraIndex  int    `json:"sura_index"`
	AyahNumber int    `json:"ayah_number"`
	SuraName   string `json:"sura_name"`
	Text       string `json:"text"`
}

func AyahDetailsResponseFromAyah(ayah *data.Ayah) *AyahDetailsResponse {
	return &AyahDetailsResponse{
		SuraIndex:  ayah.Sura.Index,
		SuraName:   ayah.Sura.Name,
		AyahNumber: ayah.Number,
		Text:       ayah.Text,
	}
}

type TafseerDetails struct {
	Id       int    `json:"id"`
	Name     string `json:"name"`
	Language string `json:"language"`
	Author   string `json:"author"`
	BookName string `json:"book_name"`
}

type TafseerListDetailsResponse []TafseerDetails

type AyahTafseerResponse struct {
	TafseerId   int    `json:"tafseer_id"`
	TafseerName string `json:"tafseer_name"`
	AyahUrl     string `json:"ayah_url"`
	AyahNumber  int    `json:"ayah_number"`
	Text        string `json:"text"`
}

// AyahTafseerResponseFromTafseer Convert TafseerText to AyahTafseerResponse
func AyahTafseerResponseFromTafseer(t *data.TafseerText) *AyahTafseerResponse {
	return &AyahTafseerResponse{
		TafseerId:   t.Id,
		TafseerName: t.Tafseer.Name,
		AyahUrl:     t.GetAyahUrl(),
		AyahNumber:  t.Ayah.Number,
		Text:        t.Text,
	}

}

type AyahTafseerListResponse []AyahTafseerResponse

func AyahTafseerListResponseFromTafseerText(ts []*data.TafseerText) *AyahTafseerListResponse {
	var tafseer AyahTafseerListResponse
	for _, t := range ts {
		detail := AyahTafseerResponse{
			TafseerId:   t.Id,
			TafseerName: t.Tafseer.Name,
			AyahUrl:     t.GetAyahUrl(),
			AyahNumber:  t.Ayah.Number,
			Text:        t.Text,
		}
		tafseer = append(tafseer, detail)
	}
	return &tafseer
}
