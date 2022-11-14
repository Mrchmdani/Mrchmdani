package controllers

import (
	"Tasking-golang/database"
	"Tasking-golang/models"
	"github.com/gin-gonic/gin"
	"net/http"
	"strconv"
)

type NoteController struct{}

func (NoteController) Root(c *gin.Context) {
	c.Redirect(http.StatusFound, "/notes")
}

func (NoteController) Index(c *gin.Context) {
	db := database.Instance()

	query := c.DefaultQuery("q", "")
	var notes []models.Note
	db.Where("Content LIKE ?", "%"+query+"%").
		Find(&notes) //SEARCHBAR

	c.HTML(http.StatusOK, "notes/index", gin.H{
		"title": "Notes Index",
		"query": query, //default name in search bar so it stay
		"notes": notes,
	})
}
func (NoteController) Create(c *gin.Context) {
	db := database.Instance()
	user := c.PostForm("user")
	content := c.PostForm("content")

	db.Create(&models.Note{User: user, Content: content})

	c.Redirect(http.StatusFound, "/notes")
}

func (NoteController) Detail(c *gin.Context) {
	db := database.Instance()
	id, _ := strconv.Atoi(c.Param("id"))

	var note models.Note
	result := db.First(&note, id)

	if result.RowsAffected == 0 {
		c.JSON(http.StatusNotFound, gin.H{
			"message": "Data not found!",
		})
	} else {
		c.JSON(http.StatusOK, gin.H{
			"message": "Data successfully!",
			"note":    note,
		})
	}
}
func (NoteController) Edit(c *gin.Context) {
	db := database.Instance()
	id, _ := strconv.Atoi(c.Param("id"))
	content := c.PostForm("content")

	db.Model(&models.Note{}).
		Where("id  = ?", id).
		Update("content", content)

	c.JSON(http.StatusOK, gin.H{
		"message": "Data updated!",
	})
}

func (NoteController) Delete(c *gin.Context) {
	db := database.Instance()
	id, _ := strconv.Atoi(c.Param("id"))

	db.Delete(&models.Note{}, id)

	c.Redirect(http.StatusFound, "/notes")
}
func (NoteController) Done(c *gin.Context) {
	db := database.Instance()
	id, _ := strconv.Atoi(c.Param("id"))

	var note models.Note
	db.Find(&note, id)

	note.IsDone = !note.IsDone

	db.Save(&note)

	c.Redirect(http.StatusFound, "/notes")
}
