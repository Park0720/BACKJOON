import sys

input = sys.stdin.readline

N, M = map(int,input().strip().split())
arr = list(map(int,input().strip().split()))

l = 0
r = 2000000000

while l<=r:
    mid = (l+r)//2
    tree_sum = sum(arr[i]-mid if arr[i]>mid else 0 for i in range(N))
    # print(mid)
    if tree_sum>=M:
        l = mid+1
    else:
        r = mid-1

print(r)