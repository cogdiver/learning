package modulos

import (
	"fmt"
	pk "study/mypackage"
)

type car struct {
	brand string
	year  int
}

func Modulo4() {
	myCar := car{"Ford", 2020}
	fmt.Println(myCar)

	// modificadores de acceso
	var myCar2 pk.CarPublic
	// var myCar3 pk.carPrivate

	myCar2.Brand = "Ferrari"
	myCar2.Year = 2020
	fmt.Println(myCar2)

	pk.PrintMessage("Hola, platzi")
}
