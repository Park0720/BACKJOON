A, B, V = map(int, input().split())

answer = (V-B) / (A-B)

if answer == int(answer):
    print(int(answer))
else:
    print(int(answer) + 1)