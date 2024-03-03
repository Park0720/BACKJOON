E, S, M = map(int, input().split())

i = 0
e, s, m = 0, 0, 0
while True:
    if e == E and s == S and m == M:
        break
    i += 1
    e += 1
    s += 1
    m += 1

    if e >= 16:
        e = 1
    if s >= 29:
        s = 1
    if m >= 20:
        m = 1


print(i)