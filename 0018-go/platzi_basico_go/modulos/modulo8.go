package modulos

import "fmt"

func say2(text string, c chan<- string) {
	c <- text
}

func message(text string, c chan<- string) {
	c <- text
}

func Modulo8() {
	c := make(chan string, 1)
	fmt.Println("Hello")
	go say2("Bye", c)
	fmt.Println(<-c)
	close(c)

	c2 := make(chan string, 2)
	c2 <- "mensaje1"
	c2 <- "mensaje2"
	fmt.Println(len(c2), cap(c2))

	// range y close
	close(c2)
	for m := range c2 {
		fmt.Println(m)
	}

	// select
	e1 := make(chan string)
	e2 := make(chan string)
	go message("mensaje1", e1)
	go message("mensaje2", e2)
	for i := 0; i < 2; i++ {
		select {
		case m1 := <-e1:
			fmt.Println("message de e1", m1)
		case m2 := <-e2:
			fmt.Println("message de e2", m2)
		}
	}
}
