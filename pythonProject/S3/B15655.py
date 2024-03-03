def perm(level):
    if level == M:
        sort_path = sorted(path)
        if sort_path == path:
            print(*path)
        return

    for i in range(N):
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
