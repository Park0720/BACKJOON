N = int(input())

i = 0
_sum = 0
while True:
    if _sum > N:
        break
    i += 1
    _sum += i

print(i-1)