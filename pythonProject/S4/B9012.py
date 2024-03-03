T = int(input())

for test_case in range(1, T+1):
    word = input()
    stack = []
    flag = True
    for letter in word:
        if letter == '(':
            stack.append(letter)
        elif letter == ')':
            if len(stack) > 0:
                stack.pop()
            elif len(stack) == 0:
                flag = False
                break

    if flag and len(stack) == 0:
        print('YES')
    else:
        print('NO')