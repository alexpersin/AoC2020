package main

import (
	"fmt"
)

// Cup is a linked list node
type Cup struct {
	val int
	nxt *Cup
}

func main() {
	MAX := 1000000
	ROUNDS := 10000000
	data := []int{9, 5, 2, 3, 1, 6, 4, 8, 7}
	lookup := make(map[int]*Cup)
	var prev *Cup
	var first *Cup

	for i := 0; i < len(data); i++ {
		c := &Cup{val: data[i]}
		lookup[data[i]] = c
		if prev != nil {
			prev.nxt = c
		} else {
			first = c
		}
		prev = c
	}

	var c *Cup
	for i := 10; i <= MAX; i++ {
		c = &Cup{val: i}
		prev.nxt = c
		lookup[i] = c
		prev = c
	}
	c.nxt = first
	current := first

	var destination int
	for i := 0; i < ROUNDS; i++ {
		removed := []*Cup{current.nxt, current.nxt.nxt, current.nxt.nxt.nxt}
		current.nxt = current.nxt.nxt.nxt.nxt
		if current.val > 1 {
			destination = current.val - 1
		} else {
			destination = MAX
		}
		for {
			if destination != removed[0].val && destination != removed[1].val && destination != removed[2].val {
				break
			}
			destination--
			if destination == 0 {
				destination = MAX
			}
		}
		dcup := lookup[destination]
		after := dcup.nxt
		dcup.nxt = removed[0]
		removed[2].nxt = after
		current = current.nxt
	}
	a := lookup[1].nxt.val
	b := lookup[1].nxt.nxt.val
	fmt.Println(a * b)
	// answer 363807398885
}
