package models

import (
	"gorm.io/gorm"
	"time"
)

type Note struct {
	ID        uint           `gorm:"primaryKey;autoIncrement:true" json:"id"`
	User      string         `json:"user"`
	Content   string         `json:"content"`
	DueDate   time.Time      `json:"duedate"`
	IsDone    bool           `json:"isdone"`
	CreatedAt time.Time      `json:"created_at"`
	UpdatedAt time.Time      `json:"updated_at"`
	DeletedAt gorm.DeletedAt `gorm:"index" json:"deleted_at"`
}
