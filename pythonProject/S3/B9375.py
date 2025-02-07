import sys

T = int(sys.stdin.readline().strip())

for _ in range(T):
    case = {}
    result = 1

    n = int(sys.stdin.readline().strip())

    for _ in range(n):
        wear, wear_type = sys.stdin.readline().strip().split()

        if not wear_type in case:
            case[wear_type] = 1
        else:
            case[wear_type] += 1

    for i in case:
        result *= (case[i] + 1)

    print(result-1)