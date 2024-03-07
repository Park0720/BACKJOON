i = 0
while True:
    stack = []
    i += 1
    flag = True
    word = input()
    if word == '.':
        break

    for char in word:
        if char == '(' or char == '[':
            stack.append(char)
        elif char == ')':
            if stack:
                bracket = stack.pop()
                if bracket == '[':
                    flag = False
                    break
            else:
                flag = False
                break
        elif char == ']':
            if stack:
                bracket = stack.pop()
                if bracket == '(':
                    flag = False
                    break
            else:
                flag = False
                break

    if stack:
        print('no')
        continue

    if not flag:
        print('no')
    else:
        print('yes')
