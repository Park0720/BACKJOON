N = int(input())

point_list = [list(map(int, input().split())) for _ in range(N)]

point_list.sort()

for point in point_list:
    print(*point)