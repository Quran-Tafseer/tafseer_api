package data

import (
	"gorm.io/gorm"
)

type Sura struct {
	Index int
	Name  string
	Ayahs []Ayah `gorm:"foreignKey:SuraId;references:Index"`
}

func (Sura) TableName() string {
	return "quran_text_sura"
}

type Ayah struct {
	Id     int
	Number int
	Text   string
	SuraId int
	Sura   Sura `gorm:"foreignKey:Index;references:SuraId"`
}

func (Ayah) TableName() string {
	return "quran_text_ayah"
}

type QuranRepository interface {
	GetSuras() ([]Sura, error)
	GetAyah(surahIndex string, ayahNumber string) (*Ayah, error)
}

type quranRepository struct {
	db *gorm.DB
}

func NewQuranRepository(db *gorm.DB) QuranRepository {
	return &quranRepository{db: db}
}

func (q *quranRepository) GetSuras() ([]Sura, error) {
	var suras []Sura
	res := q.db.Find(&suras)
	if res.Error != nil {
		return nil, res.Error
	}

	return suras, nil
}

func (q *quranRepository) GetAyah(surahIndex string, ayahNumber string) (*Ayah, error) {
	var ayah Ayah

	res := q.db.Preload("Sura").Where("sura_id = ? AND number = ?", surahIndex, ayahNumber).First(&ayah)
	if res.Error != nil {
		return nil, res.Error
	}

	return &ayah, nil
}
