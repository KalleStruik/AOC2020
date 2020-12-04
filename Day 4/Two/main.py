#!/bin/python

EYE_COLORS = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def print_passport(data):
    print(f"byr: {data['byr']}, iyr: {data['iyr']}, eyr: {data['eyr']}, hgt: {data['hgt']}, hcl: {data['hcl']}, ecl: {data['ecl']}, pid: {data['pid']}")

def validate_passport(data):
    try:
        byr = int(data["byr"])
        if byr < 1920 or byr > 2002:
            return False
        
        iyr = int(data["iyr"])
        if iyr < 2010 or iyr > 2020:
            return False

        eyr = int(data["eyr"])
        if eyr < 2020 or eyr > 2030:
            return False
        
        hgt = data["hgt"]
        if hgt.endswith("cm"):
            hgt = int(hgt[:-2])
            if hgt < 150 or hgt > 193:
                return False
        elif hgt.endswith("in"):
            hgt = int(hgt[:-2])
            if hgt < 59 or hgt > 76:
                return False
        else:
            return False

        hcl = data["hcl"]
        if hcl.startswith("#"):
            int(hcl[1:], 16)
        else:
            return False

        ecl = data["ecl"]
        if ecl not in EYE_COLORS:
            return False

        pid = data["pid"]
        if len(pid) == 9:
            int(pid)
        else:
            return False

        print_passport(data)
        return True
    except:
        return False




with open("input", 'r') as input:
    passport_data = {}
    required_field_count = 7
    valid = 0
    for line in input:
        if line == "\n":
            if validate_passport(passport_data):
                valid += 1
            passport_data = {}
        else:
            parts = line.strip().split(" ")
            for part in parts:
                part = part.split(":")
                if not part[0] == "cid":
                    passport_data[part[0]] = part[1]
    
    if validate_passport(passport_data):
        valid += 1

    print(f"Valid: {valid}")
