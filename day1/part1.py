def main():
    with open('input', 'r') as file:
        numbers = file.readlines()

    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            if (int(numbers[i]) + int(numbers[j]) == 2020):
                print(int(numbers[i]) * int(numbers[j]))
                return 0
                
if (__name__ == '__main__'):
    main()
