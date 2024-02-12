A, B = map(str, input().split())

if A[::-1] > B[::-1]:
    print(int(A[::-1]))
else:
    print(int(B[::-1]))