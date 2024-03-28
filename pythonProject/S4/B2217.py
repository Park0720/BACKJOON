import sys

N = int(sys.stdin.readline().strip())

weight_list = []
for i in range(N):
    weight_list.append(int(sys.stdin.readline().strip()))

weight_list.sort()

answer = []
for weight in weight_list:
    answer.append(weight * N)
    N -= 1

print(max(answer))