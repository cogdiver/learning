package modulos

import (
	"fmt"
	"strconv"
)

func doubleReturn(a int) (c, d int) {
	c = a + 2
	d = a - 2
	return
}

func Modulo1() {

	const pi float64 = 3.14
	fmt.Println(pi)

	fmt.Println("Hello World 2")
	c := 10 + 8i

	fmt.Println(c)
	fmt.Println(doubleReturn(10))

	for i := 0; i < 5; i++ {
		fmt.Println(i)
	}

	fmt.Println("-----------------------------")

	counter := 0
	for counter < 5 {
		fmt.Println(counter)
		counter++
	}

	x := 0
	if x != 0 {
		fmt.Println("es cero")
	} else {
		fmt.Println("no es cero")
	}

	// convertir texto a entero
	value, err := strconv.Atoi("53")
	fmt.Println(value, err)

	// switch
	modulo := 5 % 2
	switch modulo {
	case 0:
		fmt.Println("es par")
	default:
		fmt.Println("es impar")
	}

	switch modulo := 4 % 2; modulo {
	case 0:
		fmt.Println("es par")
	default:
		fmt.Println("es impar")
	}

	value2 := 200
	switch {
	case value2 > 150:
		fmt.Println("es mayor a 150")
	default:
		fmt.Println("no es mayor a 150")
	}
}
