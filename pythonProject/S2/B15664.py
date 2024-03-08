def perm(level):
    if level == M:
        if path not in answer:
            answer.append(path[:])
        return

    for i in range(N):
        if level > 0 and path[level - 1] > arr[i]:  # 순열이 오름차순이 아닌 경우 건너뜁니다.
            continue
        if used[i]:
            continue
        used[i] = True
        path.append(arr[i])
        perm(level+1)
        path.pop()
        used[i] = False


N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
used = [False for _ in range(N)]
path = []
answer = []

perm(0)

for i in range(len(answer)):
    print(*answer[i])