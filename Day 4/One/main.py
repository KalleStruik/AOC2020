#!/bin/python

def print_passport(data):
    print(f"byr: {data['byr']}, iyr: {data['iyr']}, eyr: {data['eyr']}, hgt: {data['hgt']}, hcl: {data['hcl']}, ecl: {data['ecl']}, pid: {data['pid']}")

with open("input", 'r') as input:
    passport_data = {}
    required_field_count = 7
    valid = 0
    for line in input:
        if line == "\n":
            if len(passport_data) == required_field_count:
                valid += 1
            passport_data = {}
        else:
            parts = line.strip().split(" ")
            for part in parts:
                part = part.split(":")
                if not part[0] == "cid":
                    passport_data[part[0]] = part[1]
    
    if len(passport_data) == required_field_count:
        valid += 1

    print(f"Valid: {valid}")
