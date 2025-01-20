import sys

N, M = map(int, sys.stdin.readline().split())

passwords = {}

for i in range(N):
    site, password = map(str, sys.stdin.readline().split())
    passwords[site] = password

for j in range(M):
    want_site = sys.stdin.readline().strip()
    sys.stdout.write(passwords[want_site] + '\n')
