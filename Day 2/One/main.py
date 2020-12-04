#!/bin/python

with open("input", 'r') as input:
    counter = 0
    for line in input:
        parts = line.split(": ")
        policy = parts[0].split(" ")
        policy_amount = policy[0].split("-")
        min_amount = int(policy_amount[0])
        max_amount = int(policy_amount[1])
        char = policy[1]
        password = parts[1]

        amount = password.count(char)
        if amount >= min_amount and amount <= max_amount:
            counter += 1

    print(f"Counter: {counter}")
