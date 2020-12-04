#!/bin/python

with open("input", 'r') as input:
    counter = 0
    for line in input:
        parts = line.split(": ")
        policy = parts[0].split(" ")
        policy_pos = policy[0].split("-")
        pos_one = int(policy_pos[0]) - 1
        pos_two = int(policy_pos[1]) - 1
        char = policy[1]
        password = parts[1]

        if (password[pos_one] == char and not password[pos_two] == char) or (password[pos_two] == char and not password[pos_one] == char):
            counter += 1

    print(f"Counter: {counter}")
