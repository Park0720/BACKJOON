import sys

input = sys.stdin.readline

N, M = map(int, input().strip().split())
number_list = list(map(int, input().strip().split()))
answer_list = [0]
tmp = 0

for i in number_list:
    tmp = tmp + i
    answer_list.append(tmp)

for _ in range(M):
    i, j = map(int, input().strip().split())
    print(answer_list[j] - answer_list[i-1])