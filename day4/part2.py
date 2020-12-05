import re

def check_byr(passport):
    return int(passport['byr']) in range(1920, 2003)

def check_iyr(passport):
    return int(passport['iyr']) in range(2010, 2021)

def check_eyr(passport):
    return int(passport['eyr']) in range(2020, 2031)

def check_hgt(passport):
    if('cm' in passport['hgt']):
       return int(passport['hgt'][:-2]) in range(150, 194)
    elif ('in' in passport['hgt']):
        return int(passport['hgt'][:-2]) in range(59, 77)
    return False

def check_hcl(passport):
    if (passport['hcl'][0] == '#'):
        if len(passport['hcl'][1:]) == 6:
            return re.match('[0-9a-f]{6}', passport['hcl'][1:])
    return False

def check_ecl(passport):
    ecl = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    return passport['ecl'] in ecl

def check_pid(passport):
    return len(passport['pid']) == 9

def main():
    with open("input", "r") as file:
        data = file.readlines()
        for i in range(len(data)):
            data[i] = data[i].replace(" ", "\n")

    with open("input", "w") as file:
        file.writelines(data)

    with open("input", "r") as file:
        data = file.readlines()

    valid = 0
    passport = {}
    count = 0
    
    while count < len(data):
        while (count != len(data) and data[count] != '\n'):
            key, value = data[count].split(':')
            value = value.rstrip('\n')
            passport[key] = value
            count += 1
        if len(passport) == 8 or (len(passport) == 7 and "cid" not in passport):
            if check_byr(passport):
                if check_iyr(passport):
                    if check_eyr(passport):
                        if check_hgt(passport):
                            if check_hcl(passport):
                                if check_ecl(passport):
                                    if check_pid(passport):
                                        valid += 1
        count +=1
        passport = {}

    print(valid)
    
if (__name__ == '__main__'):
    main()
