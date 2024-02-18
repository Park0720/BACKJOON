N = int(input())

member = [list(map(str, input().split())) for _ in range(N)]

for i in range(N):
    member[i].append(i)
    member[i][0] = int(member[i][0])
    member[i][1], member[i][2] = member[i][2], member[i][1]


member.sort()

for i in range(N):
    print(member[i][0], member[i][2])