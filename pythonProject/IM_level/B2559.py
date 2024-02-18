N, K = map(int, input().split())
temp_list = list(map(int, input().split()))

sum_temp = sum(temp_list[:K])  # 첫 K개 원소의 합
max_temp = sum_temp  # 최대 합

for i in range(K, N):
    sum_temp = sum_temp - temp_list[i-K] + temp_list[i]
    max_temp = max(max_temp, sum_temp)  # 최대 합 갱신

print(max_temp)


# N, K = map(int, input().split())
#
# temp_list = list(map(int, input().split()))
#
# max_temp = -100
#
# for i in range(N-(K-1)):
#     sum_temp = 0
#     for j in range(K):
#         sum_temp += temp_list[i+j]
#     if sum_temp > max_temp:
#         max_temp = sum_temp
#
# print(max_temp)