package modulos

import "fmt"

func Worker(id int, jobs <-chan int, results chan<- int) {
	for job := range jobs {
		fmt.Printf("Worker with id %d started fib with %d\n", id, job)
		fib := Fibonacci_(job)
		fmt.Printf("Worker with id %d, job %d and fib %d\n", id, job, fib)
		results <- fib
	}
}

func Fibonacci_(n int) int {
	if n <= 1 {
		return n
	}
	return Fibonacci_(n-1) + Fibonacci_(n-2)
}

func Modulo7() {
	tasks := []int{2, 3, 4, 5, 7, 10, 12, 40}
	nWorkers := 3
	jobs := make(chan int, len(tasks))
	results := make(chan int, len(tasks))

	for i := 0; i < nWorkers; i++ {
		go Worker(i, jobs, results)
	}

	for _, value := range tasks {
		jobs <- value
	}
	close(jobs)

	for r := 0; r < len(tasks); r++ {
		<-results
	}
}
