// two arrays to hold the room
// each row depends on itself and its neighbours
// for each row, create a goroutine to update the array
// go routine send a message when its done to its nieghbours
// go routine receives a message to start when its neighbours are both done with
// the previous round

package main

import (
	"bufio"
	"fmt"
	"os"
)

const (
	floor    = 0
	chair    = 1
	occupied = 2
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func printArr(a [][]int) {
	m := map[int]rune{
		floor:    '.',
		chair:    'L',
		occupied: '#',
	}
	for _, row := range a {
		for _, c := range row {
			fmt.Printf("%c", m[c])
		}

		fmt.Print("\n")
	}
}

func noOccupied(a [][]int, x, y int) bool {

	for i := x - 1; i <= x+1; i++ {
		for j := y - 1; j <= y+1; j++ {
			fmt.Println(i, j)
			if a[i][j] == occupied {
				return false
			}
		}
	}
	return true
}

func fourOccupied(a [][]int, x, y int) bool {
	count := 0
	for i := x - 1; i <= x+1; i++ {
		for j := y - 1; j <= y+1; j++ {
			if a[i][j] == occupied {
				count++
				if count == 4 {
					return true
				}
			}
		}
	}
	return false
}

func updateRow(a, b [][]int, i int) {
	for j := 1; j < len(a[i])-1; j++ {
		c := a[i][j]
		fmt.Print(c)
		switch c {
		case chair:
			if noOccupied(a, i, j) {
				b[i][j] = occupied
			}
		case occupied:
			if fourOccupied(a, i, j) {
				b[i][j] = chair
			}
		default:
			b[i][j] = a[i][j]
		}
	}
}

func main() {

	file, err := os.Open("inputs/11")
	check(err)
	scanner := bufio.NewScanner(file)

	var a [][]int
	var b [][]int

	m := map[rune]int{
		'.': floor,
		'L': chair,
		'#': occupied,
	}

	var l int
	a = append(a, make([]int, l))
	for scanner.Scan() {
		text := scanner.Text()
		l = len(text) + 2
		inner := make([]int, l)
		for i, c := range text {
			inner[i+1] = m[c]
		}
		a = append(a, inner)
	}
	a = append(a, make([]int, l))

	file, err = os.Open("inputs/11")
	check(err)
	scanner = bufio.NewScanner(file)
	b = append(b, make([]int, l))
	for scanner.Scan() {
		text := scanner.Text()
		inner := make([]int, l)
		for i, c := range text {
			inner[i+1] = m[c]
		}
		b = append(b, inner)
	}
	b = append(b, make([]int, l))

	for i := 1; i <= len(a)-1; i++ {
		fmt.Println(a[i])
		updateRow(a, b, i)
	}

	// printArr(a)
	printArr(b)
}
