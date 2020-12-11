def main():
    with open('input', 'r') as file:
        answers = [line.rstrip() for line in file]
    
    answers.append('')
    group = []
    count = 0
    for ans in answers:
        if (ans == ''):
            combined = set(group[0])
            for i in range(len(group) - 1):
                if (i != len(group) - 1):
                    combined &= set(group[i + 1])
            count += len(list(combined))
            group = []
        else:
            group.append(ans)
    
    
    print(count)

if (__name__ == '__main__'):
    main()
