package main

import (
	"testing"
)

func TestSum(t *testing.T) {
	tables := []struct {
		a int
		b int
		n int
	}{
		{1, 2, 3},
		{5, 20, 25},
		{10, 11, 21},
	}

	for _, item := range tables {
		total := MainSum(item.a, item.b)
		if total != item.n {
			t.Errorf("Sum was incorrect, got %v expected %d", total, item.n)
		}
	}
}
