_min = 2000
for i in range(3):
    a = int(input())
    if _min > a:
        _min = a

_min_water = 2000
for i in range(2):
    a = int(input())
    if _min_water > a:
        _min_water = a

print(_min_water + _min - 50)