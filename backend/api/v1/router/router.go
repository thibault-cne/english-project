package router

import (
	"backend/api/v1/handlers/auth"

	"github.com/gin-gonic/gin"
)

func Route(engine *gin.Engine) {
	path := engine.Group("/api/v1")

	auth.LoadRoutes(path)
}
