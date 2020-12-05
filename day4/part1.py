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
            passport[key] = value
            count += 1
        if len(passport) == 8 or (len(passport) == 7 and "cid" not in passport):
            valid += 1
        count += 1
        passport = {}

    print(valid)
    
if (__name__ == '__main__'):
    main()
