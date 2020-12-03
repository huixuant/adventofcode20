def main():
    with open('input', 'r') as file:
        numbers = file.readlines()

    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            for k in range(j, len(numbers)): 
                if (int(numbers[i]) + int(numbers[j]) + int(numbers[k]) == 2020):
                    print(int(numbers[i]) * int(numbers[j]) * int(numbers[k]))
                    return 0
                
if (__name__ == '__main__'):
    main()
