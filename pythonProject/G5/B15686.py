# import sys
#
#
# def brute_force(level):
#     global min_distance
#     if level == M:
#         distance = 0
#         for house in house_list:
#             dist_house = int(1e25)
#             for chicken in chicken_list:
#                 dist_house = min(dist_house, abs(house[0]-chicken[0]) + abs(house[1]-chicken[1]))
#
#             distance += dist_house
#         min_distance = min(min_distance, distance)
#         return
#
#     for i in range(level, len(chicken_list)):
#         brute_force(level+1)
#
#
# N, M = map(int, sys.stdin.readline().split())
#
# base_list = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
#
# chicken_list = []
# house_list = []
#
# for i in range(N):
#     for j in range(N):
#         if base_list[i][j] == 2:
#             chicken_list.append([i, j])
#         elif base_list[i][j] == 1:
#             house_list.append([i, j])
#
# min_distance = int(1e25)
#
# brute_force(0)
# print(min_distance)


from itertools import combinations
import sys

N, M = map(int, sys.stdin.readline().split())
base_list = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

chicken_list = []
house_list = []

for i in range(N):
    for j in range(N):
        if base_list[i][j] == 2:
            chicken_list.append([i, j])
        elif base_list[i][j] == 1:
            house_list.append([i, j])

min_distance = int(1e25)

for chickens in combinations(chicken_list, M):
    distance = 0
    for house in house_list:
        dist_house = min(abs(house[0]-chicken[0]) + abs(house[1]-chicken[1]) for chicken in chickens)
        distance += dist_house
    min_distance = min(min_distance, distance)

print(min_distance)
