def perm(level):
    if level == M:
        print(*path)
        return

    for i in range(1, N+1):
        if used[i]:
            continue
        used[i] = True
        path.append(i)
        perm(level+1)
        path.pop()
        used[i] = False


N, M = map(int, input().split())
used = [False for _ in range(N+1)]
path = []

perm(0)
