N = int(input())

first_list = list(map(int, input().split()))
second_list = list(map(int, input().split()))

first_list.sort()
second_list.sort(reverse=True)

answer = 0
for i in range(N):
    answer += first_list[i] * second_list[i]

print(answer)