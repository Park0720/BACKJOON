A, B, V = map(int, input().split())

answer = V - (A-B) * B

if V == A:
    answer = 1
print(answer)