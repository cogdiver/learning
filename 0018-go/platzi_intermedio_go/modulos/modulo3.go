package modulos

import (
	"fmt"
	"time"
)

func sum(values ...int) int {
	total := 0
	for _, num := range values {
		total += num
	}
	return total
}

func printNames(names ...string) {
	for _, name := range names {
		fmt.Println(name)
	}
}

func getValues(x int) (double int, triple int, quad int) {
	double = 2 * x
	triple = 3 * x
	quad = 4 * x
	return
}

func Modulo3() {
	// funciones anonimas
	c := make(chan int)
	go func() {
		fmt.Println("Starting Function")
		time.Sleep(2 * time.Second)
		fmt.Println("End")
		c <- 1
	}()
	<-c

	// Funciones variadicas
	fmt.Println(sum(1))
	fmt.Println(sum(1, 2))
	fmt.Println(sum(1, 2, 3, 4))
	printNames("Alice", "Bob", "Charlie", "Dave")
	fmt.Println(getValues(2))
}
