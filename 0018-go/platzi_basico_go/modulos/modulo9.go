package modulos

import (
	"fmt"
	"net/http"
	"os"

	"github.com/labstack/echo"
)

func Modulo9() {
	args := os.Args
	fmt.Println(args[1:])

	// instanciar echo
	e := echo.New()

	// Ruta
	e.GET("/", func(c echo.Context) error {
		return c.String(http.StatusOK, "Hi, hi!")
	})
	e.Logger.Fatal(e.Start(":1323"))
}
