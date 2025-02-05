import sys
sys.setrecursionlimit(100000)

def fact(n):
    if n == 0 or n == 1:
        return 1

    return n * fact(n - 1)

N = int(input())

answer = 0
i = N
j = 0

while i >= j:
    answer += (fact(i) // (fact(j) * fact(i - j))) * (2 ** j)
    i -= 1
    j += 1

print(answer % 10007)