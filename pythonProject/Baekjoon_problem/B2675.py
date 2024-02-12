T = int(input())

for test_case in range(1, T+1):
    R, S = map(str, input().split())

    for i in range(len(S)):
        for j in range(int(R)):
            print(S[i], end='')
    print()