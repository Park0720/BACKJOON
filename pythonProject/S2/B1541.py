import sys
sys.setrecursionlimit(10 ** 8)


def _sum(x):
    if x == 1:
        return x

    return x + _sum(x-1)


i = 1
N = int(input())
while True:
    answer = _sum(i)
    if answer > N:
        i -= 1
        break
    i += 1

print(i)