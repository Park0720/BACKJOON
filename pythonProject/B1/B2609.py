x, y = map(int, input().split())

_min = x
if x > y:
    _min = y

least_mul = 1
greatest_div = 1
i = 2
while True:
    if x % i == 0 and y % i == 0:
        least_mul *= i
        x //= i
        y //= i
    else:
        i += 1
    if i > x or i > y:
        break

greatest_div = least_mul * x * y

print(least_mul)
print(greatest_div)