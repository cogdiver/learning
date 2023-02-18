package modulos

import "fmt"

func Modulo3() {
	// array
	var array [4]int
	array[0] = 1
	array[1] = 2
	fmt.Println(array, len(array), cap(array))

	// slice
	slice := []int{1, 2, 3, 4}
	slice = append(slice, 10)
	slice = append(slice, []int{20, 21}...)
	fmt.Println(slice)

	for i, v := range slice {
		fmt.Println(i, v)
	}

	// maps
	m := make(map[string]int)
	m["valentina"] = 23
	m["pepito"] = 30
	fmt.Println(m)
}
