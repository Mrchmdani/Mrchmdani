package main

import (
	"Tasking-golang/controllers"
	"github.com/gin-gonic/gin"
)

func Routes(r *gin.Engine) {
	noteController := controllers.NoteController{}

	r.GET("/", noteController.Root)

	r.GET("/notes", noteController.Index)
	r.POST("/notes", noteController.Create)

	r.GET("/notes/:id", noteController.Detail)
	r.POST("/notes/:id", noteController.Edit)

	r.GET("/notes/:id/delete", noteController.Delete)
	r.GET("/notes/:id/done", noteController.Done)
}
