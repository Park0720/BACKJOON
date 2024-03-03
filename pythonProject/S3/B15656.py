def perm(level):
    if level == M:
        print(*path)
        return

    for i in range(N):
        path.append(arr[i])
        perm(level+1)
        path.pop()


N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
path = []
answer = []

perm(0)
