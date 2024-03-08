import sys

def perm(level):
    if level == M:
        if path not in answer:
            answer.append(path[:])
        return

    for i in range(N):
        used[i] = True
        path.append(arr[i])
        perm(level+1)
        path.pop()

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
used = [False for _ in range(N)]
path = []
answer = []

perm(0)

for i in range(len(answer)):
    print(*answer[i])
