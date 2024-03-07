X = int(input())

i = 0
while True:
    if X == 1:
        break
    if X % 3 == 0:
        X //= 3
        i += 1
        if X == 1:
            break
    if X % 2 == 0:
        X //= 2
        i += 1
        if X == 1:
            break

    X -= 1
    i += 1

print(i)