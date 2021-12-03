locals {
    length = length(split("\n", chomp(file("input.txt"))))
    count_of_ones = [for i in range(12) : length([for row in split("\n", chomp(file("input.txt"))) : split("", row)[i] if split("", row)[i] == "1"])]
    gamma = parseint(join("", [for i in local.count_of_ones : i > local.length / 2 ? 1 : 0]), 2)
    epsilon = parseint(join("", [for i in local.count_of_ones : i < local.length / 2 ? 1 : 0]), 2)
    answer = local.gamma * local.epsilon
}

output answer {
  value       = local.answer
}
