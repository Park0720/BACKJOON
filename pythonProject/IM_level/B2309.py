
# # Ver 1
# from itertools import combinations
#
# small_list = []
# for _ in range(9):
#     small_list.append(int(input()))
#
# hundred_list = list(combinations(small_list, 7))
#
# for val in hundred_list:
#     val = list(val)
#     val.sort()
#     if sum(val) == 100:
#         print(*val, sep='\n')
#         break

# # Ver 2
# def subset(i, k, subset_sum, target):
#     # 합이 목표치를 넘어가는 경우 더 이상 고려할 필요 없음
#     if subset_sum > target:
#         return
#     if i == k:
#         if subset_sum != target:
#             return
#         # 합이 목표치랑 같다면
#         if subset_sum == target:
#             for j in range(k):
#                 if bit[j]:
#                     answer_list.append(small_list[j])
#             if len(answer_list) == 7:
#                 answer_list.sort()
#                 for answer in answer_list:
#                     print(answer)
#     else:
#         # for j in range(1, -1, -1):
#         #     bit[i] = j
#         #     f(i+1, k, target)
#         # 다음 수를 포함 하기로 한 경우
#         bit[i] = 1
#         subset(i+1, k, subset_sum+small_list[i], target)
#         # 다음 수를 포함하지 않기로 한 경우
#         bit[i] = 0
#         subset(i+1, k, subset_sum, target)
#
#
# N = 9
# small_list = []
# for i in range(N):
#     small_list.append(int(input()))
# answer_list = []
# bit = [0] * N
# T = 100
# subset(0, N, 0, T)

# Ver 3
N = 9
small_list = []
for i in range(N):
    small_list.append(int(input()))

for i in small_list:
    for j in small_list:
        if i != j and sum(small_list) - i - j == 100:
            small_list.pop(small_list.index(i))
            small_list.pop(small_list.index(j))

small_list.sort()
print(*small_list, sep='\n')