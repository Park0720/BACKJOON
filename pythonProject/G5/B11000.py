import sys
import heapq
input = sys.stdin.readline

N = int(input())
time_table = [list(map(int, input().split())) for _ in range(N)]
time_table.sort()
rooms = []
heapq.heappush(rooms, time_table[0][1])

for i in range(1, N):
    if time_table[i][0] >= rooms[0]:
        heapq.heappop(rooms)
    heapq.heappush(rooms, time_table[i][1])
print(len(rooms))