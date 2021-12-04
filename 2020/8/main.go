package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

// read instructions into an array and a map. If map is true, quit
// check if instruction has been changed before, if not then change it and run
func main() {
	scanner := bufio.NewScanner(os.Stdin)

	instructions := make([]string, 633)

	i := 0
	for scanner.Scan() {
		line := scanner.Text()
		instructions[i] = line
		i++
	}

	changed := make(map[int]bool)

	// for each changed instruction
	for {
		fmt.Println("Running")
		visited := make(map[int]bool)
		cFlag := ""

		i = 0
		acc := 0
		for {
			if i == len(instructions) {
				fmt.Println("Done with accumulator", acc)
				os.Exit(0)
			}
			if visited[i] == true {
				fmt.Println("Infinite loop after changing", cFlag, acc)
				break
			}
			visited[i] = true
			ins := instructions[i]
			t := strings.Split(ins, " ")
			op, v := t[0], t[1]
			val, _ := strconv.Atoi(v)
			if cFlag == "" && changed[i] == false && (op == "jmp" || op == "nop") {
				cFlag = ins
				changed[i] = true
				fmt.Println("Changing instruction", i, ins)
				if op == "jmp" {
					op = "nop"
				} else if op == "nop" {
					op = "jmp"
				}
			}
			switch op {
			case "acc":
				acc += val
			case "jmp":
				i += val
				continue
			case "nop":
			}
			i++
		}
	}
}
