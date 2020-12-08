package main

import (
	"bufio"
	"fmt"
	"io"
	"os"
	"strconv"
	"strings"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func valid(min, max uint64, char rune, pwd string) bool {
	var count uint64 = 0
	for _, c := range pwd {
		if c == char {
			count++
		}
	}
	return (count >= min && count <= max)
}

func main() {
	file, err := os.Open("input1")
	check(err)
	defer file.Close()

	ans := 0
	reader := bufio.NewReader(file)
	var line string
	for {
		line, err = reader.ReadString('\n')
		if err != nil && err != io.EOF {
			break
		}
		if len(line) == 0 {
			break
		}

		parts := strings.Split(line, " ")
		mm := strings.Split(parts[0], "-")
		min, _ := strconv.ParseUint(mm[0], 10, 64)
		max, _ := strconv.ParseUint(mm[1], 10, 64)
		char := rune(parts[1][0])
		pwd := parts[2]
		// fmt.Println(min, max, char, pwd)
		// fmt.Println(valid(min, max, char, pwd))
		if valid(min, max, char, pwd) {
			ans++
		}
	}
	fmt.Println(ans)
}
