import sys

def perm(level, last):
    if level == M:
        print(*path)
        return

    overlab = 0  # 이전에 사용한 숫자를 기록
    for i in range(N):
        if used[i] or arr[i] == overlab:  # 이미 사용했거나 이전에 사용한 숫자와 같다면 건너뛰기
            continue
        path.append(arr[i])
        perm(level+1, i)
        path.pop()
        overlab = arr[i]  # 사용한 숫자 기록

N, M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
arr.sort()
used = [False for _ in range(N)]
path = []

perm(0, 0)
