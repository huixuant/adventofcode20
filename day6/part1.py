def main():
    with open('input', 'r') as file:
        answers = [line.rstrip() for line in file]
    
    answers.append('')
    group = ""
    count = 0
    for ans in answers:
        if (ans == ''):
            count += len(set(group))
            group = ""
        else:
            group += ans
    
    
    print(count)

if (__name__ == '__main__'):
    main()
