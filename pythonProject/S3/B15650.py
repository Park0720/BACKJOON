def perm(level):
    if level == M:
        sort_path = sorted(path)
        if sort_path == path:
            answer.append(sort_path)
        return

    for i in range(1, N + 1):
        if used[i]:
            continue
        used[i] = True
        path.append(i)
        perm(level + 1)
        path.pop()
        used[i] = False


N, M = map(int, input().split())
used = [False for _ in range(N + 1)]
path = []
answer = []

perm(0)

for val in answer:
    print(*val)
