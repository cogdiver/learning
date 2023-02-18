package modulos

import "fmt"

func Modulo2() {
	// defer
	defer fmt.Println("Saliendo")
	fmt.Println("valor en modulo2")

	for i := 0; i < 5; i++ {
		if i == 2 {
			fmt.Println("Es dos")
			continue
		}
		for j := 0; j < 5; j++ {

			if j == 3 {
				fmt.Println("Es tres")
				break
			}
			fmt.Println(i, j)
		}
		fmt.Println(i)
	}
}
