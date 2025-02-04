import sys

X = int(sys.stdin.readline().strip())

count = 0

def calc(x, c):
    global count
    if count and c == count:
        return
    if x == 1:
        count = c
        return
    c += 1
    if x % 3 == 0:
        calc(x // 3, c)
    if x % 2 == 0:
        calc(x // 2, c)
    calc(x - 1, c)

calc(X, 0)

print(count)