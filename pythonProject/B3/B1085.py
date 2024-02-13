x, y, w, h = map(int, input().split())

_min = w - x

if _min > x:
    _min = x
if _min > h - y:
    _min = h - y
if _min > y:
    _min = y

print(_min)