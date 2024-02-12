N = int(input())

T = 1001
base_list = [[0] * T for _ in range(T)]

for i in range(1, N+1):
    paper = list(map(int, input().split()))
    for j in range(paper[0], paper[0]+paper[2]):
        for k in range(paper[1], paper[1]+paper[3]):
            base_list[j][k] = i

for i in range(1, N + 1):
    count = 0
    for j in range(T):
        for k in range(T):
            if base_list[j][k] == i:
                count += 1
    print(count)