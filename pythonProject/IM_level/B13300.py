N, K = map(int, input().split())

man_room_list = [[] for _ in range(6)]
woman_room_list = [[] for _ in range(6)]

for _ in range(N):
    S, Y = map(int, input().split())
    if S:
        man_room_list[Y-1].append(0)
    else:
        woman_room_list[Y-1].append(0)

room_count = 0
for i in range(6):
    if len(man_room_list[i]) % K == 0:
        room_count += len(man_room_list[i]) // K
    if len(woman_room_list[i]) % K == 0:
        room_count += len(woman_room_list[i]) // K
    if len(man_room_list[i]) % K != 0:
        room_count += len(man_room_list[i]) // K + 1
    if len(woman_room_list[i]) % K != 0:
        room_count += len(woman_room_list[i]) // K + 1

print(room_count)