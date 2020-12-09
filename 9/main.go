package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

// add window to map
// check n - val for each window to see if its in window
// if not, print
func p1(nums []int) int {
	scanner := bufio.NewScanner(os.Stdin)
	var valid bool
	window := make(map[int]bool)

	for scanner.Scan() {
		line, _ := strconv.Atoi(scanner.Text())
		nums = append(nums, line)
	}

	for i, num := range nums {
		if i < 25 {
			window[num] = true
			continue
		}
		valid = false
		for k := range window {
			if _, ok := window[num-k]; ok && k != num-k {
				// there exists a pair of numbers in the window that add up to num
				valid = true
				break
			}
		}
		if !valid {
			fmt.Println(num, "is not valid with window", window)
			return num
		}
		// the number is valid, now move to the next
		delete(window, nums[i-25])
		window[num] = true
	}
	return -1
}

func MinMax(array []int) (int, int) {
	var max int = array[0]
	var min int = array[0]
	for _, value := range array {
		if max < value {
			max = value
		}
		if min > value {
			min = value
		}
	}
	return min, max
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	var nums []int

	for scanner.Scan() {
		line, _ := strconv.Atoi(scanner.Text())
		nums = append(nums, line)
	}

	num := p1(nums)
	start := 0
	end := 1
	tot := nums[0] + nums[1]
	for {
		if tot > num {
			// nothing for this value of start
			start++
			end = start + 1
			tot = nums[start] + nums[end]
			continue
		} else if tot == num {
			min, max := MinMax(nums[start:end])
			fmt.Println(min + max)
			break
		} else {
			end++
			tot += nums[end]
		}
	}
}
