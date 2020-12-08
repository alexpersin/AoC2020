package main

import (
	"fmt"
	"io/ioutil"
	"regexp"
	"strconv"
	"strings"
)

func valid(doc []string) bool {
	keys := make(map[string]bool)
	for _, pair := range doc {
		keys[pair[:3]] = true
	}
	for _, req := range []string{"ecl", "hcl", "eyr", "iyr", "hgt", "byr", "pid"} {
		if _, ok := keys[req]; !ok {
			return false
		}
	}
	return true
}

var checks = map[string]func(string) bool{
	"byr": func(s string) bool {
		match, _ := regexp.MatchString(`\d{4}`, s)
		if !match {
			return false
		}
		x, err := strconv.Atoi(s)
		if err != nil {
			return false
		}
		return x >= 1920 && x <= 2002
	},
	"iyr": func(s string) bool {
		match, _ := regexp.MatchString(`\d{4}`, s)
		if !match {
			return false
		}
		x, err := strconv.Atoi(s)
		if err != nil {
			return false
		}
		return x >= 2010 && x <= 2020
	},
	"eyr": func(s string) bool {
		match, _ := regexp.MatchString(`\d{4}`, s)
		if !match {
			return false
		}
		x, err := strconv.Atoi(s)
		if err != nil {
			return false
		}
		return x >= 2020 && x <= 2030
	},
	"hgt": func(s string) bool {
		re := regexp.MustCompile(`(\d+)(in|cm)`)
		groups := re.FindStringSubmatch(s)
		// fmt.Println(groups)
		if len(groups) < 3 {
			return false
		}
		h := groups[1]
		unit := groups[2]
		if unit == "cm" {
			x, err := strconv.Atoi(h)
			if err != nil {
				return false
			}
			return x >= 150 && x <= 193
		} else if unit == "in" {
			x, err := strconv.Atoi(h)
			if err != nil {
				return false
			}
			return x >= 59 && x <= 76
		}
		return false
	},
	"hcl": func(s string) bool {
		match, _ := regexp.MatchString(`^#[0-9a-f]{6}$`, s)
		return match
	},
	"ecl": func(s string) bool {
		match, _ := regexp.MatchString(`^(amb|blu|brn|gry|grn|hzl|oth)$`, s)
		return match
	},
	"pid": func(s string) bool {
		match, _ := regexp.MatchString(`^\d{9}$`, s)
		return match
	},
}

func valid2(doc []string) bool {
	keys := make(map[string]string)
	for _, pair := range doc {
		keys[pair[:3]] = pair[4:]
	}
	for field, check := range checks {
		value, ok := keys[field]
		if field == "pid" {
			fmt.Println(field, value, check(value))
		}
		if !ok {
			return false
		}
		if !check(value) {
			return false
		}
	}
	// fmt.Println("Valid doc")
	return true
}

func main() {
	all, _ := ioutil.ReadFile("inputs/4")
	emptyLine := regexp.MustCompile(`\n\n`)
	docs := emptyLine.Split(string(all), -1)
	count := 0
	for _, doc := range docs {
		d := strings.Fields(doc)
		// fmt.Println("doc:", d)
		if valid2(d) {
			count++
		}
	}
	fmt.Println(count)
}
