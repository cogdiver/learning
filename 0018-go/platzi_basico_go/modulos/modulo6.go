package modulos

import "fmt"

type figuras2D interface {
	area() float64
}

type cuadrado struct {
	base float64
}

type rectangulo struct {
	base   float64
	altura float64
}

func (c cuadrado) area() float64 {
	return c.base * c.base
}

func (r rectangulo) area() float64 {
	return r.base * r.altura
}

func calcular(f figuras2D) {
	fmt.Println("Area:", f.area())
}

func Modulo6() {
	mySquare := cuadrado{2}
	myRect := rectangulo{2, 4}

	calcular(mySquare)
	calcular(myRect)

	// lista de interfaces
	myInterface := []interface{}{"Hola", 12, true, 1.25}
	fmt.Println(myInterface)
	fmt.Println(myInterface...)
}
