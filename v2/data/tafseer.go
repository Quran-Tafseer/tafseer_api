package data

import (
	"fmt"
	"gorm.io/gorm"
)

type Tafseer struct {
	Id       int
	Name     string
	Author   string
	BookName string
	Language string
}

func (Tafseer) TableName() string {
	return "quran_tafseer_tafseer"
}

type TafseerText struct {
	Id        int
	AyahId    int
	TafseerId int
	Text      string
	Ayah      Ayah    `gorm:"foreignKey:Id;references:AyahId"`
	Tafseer   Tafseer `gorm:"foreignKey:Id;references:TafseerId"`
}

func (TafseerText) TableName() string {
	return "quran_tafseer_tafseertext"
}

func (t TafseerText) GetAyahUrl() string {
	return fmt.Sprintf("/quran/%d/%d", t.Ayah.SuraId, t.Ayah.Number)
}

type TafseerRepository interface {
	GetTafseerList() ([]Tafseer, error)
	GetAyahTafseer(surahIndex string, ayahNumber string, tafseerId string) (*TafseerText, error)
	GetAyahRangeTafseer(surahIndex string, ayahFrom string, ayahTo string, tafseerId string) ([]*TafseerText, error)
}

type tafseerRepository struct {
	db *gorm.DB
}

func NewTafseerRepository(db *gorm.DB) TafseerRepository {
	return &tafseerRepository{db: db}
}

func (t *tafseerRepository) GetTafseerList() ([]Tafseer, error) {
	var tafseer []Tafseer

	res := t.db.Find(&tafseer)
	if res.Error != nil {
		return nil, res.Error
	}

	return tafseer, nil
}

func (t *tafseerRepository) GetAyahTafseer(surahIndex string, ayahNumber string, tafseerId string) (*TafseerText, error) {
	var tafseerText TafseerText

	res := t.db.Preload("Tafseer").Joins("Ayah").Where("\"Ayah\".id = ? AND \"Ayah\".sura_id = ? AND tafseer_id = ?", ayahNumber, surahIndex, tafseerId).Find(&tafseerText)
	if res.Error != nil {
		return nil, res.Error
	}

	return &tafseerText, nil
}

func (t *tafseerRepository) GetAyahRangeTafseer(surahIndex string, ayahFrom string, ayahTo string, tafseerId string) ([]*TafseerText, error) {
	var tafseerText []*TafseerText

	res := t.db.Preload("Tafseer").Joins("Ayah").Where("\"Ayah\".id BETWEEN ? AND ? AND \"Ayah\".sura_id = ? AND tafseer_id = ?", ayahFrom, ayahTo, surahIndex, tafseerId).Find(&tafseerText)
	if res.Error != nil {
		return nil, res.Error
	}

	return tafseerText, nil
}
