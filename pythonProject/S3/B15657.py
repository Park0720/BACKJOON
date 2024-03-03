def perm(level):
    if level == M:
        print(*path)
        return

    for i in range(N):
        if level > 0 and path[level-1] > arr[i]:  # 순열이 오름차순이 아닌 경우 건너뜁니다.
            continue

        path.append(arr[i])
        perm(level+1)
        path.pop()


N, M = map(int, input().split())
arr = sorted(list(map(int, input().split())))
path = []
perm(0)
