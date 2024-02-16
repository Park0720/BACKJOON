T = int(input())

for test_case in range(1, T+1):
    k = int(input())
    n = int(input())

    _max = k
    if k < n:
        _max = n

    arr = [[0] * (_max+1) for _ in range(_max+1)]

    for i in range(_max+1):
        for j in range(_max+1):
            if i == 0:
                arr[i][j] = j + 1
            else:
                arr[i][j] = arr[i-1][j] + arr[i][j-1]
    print(arr[k][n-1])