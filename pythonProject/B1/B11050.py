def fact(i):
    if i == 0:
        return 1
    if i == 1:
        return 1

    return i*fact(i-1)


N, K = map(int, input().split())

answer = fact(N) // (fact(K) * (fact(N-K)))

print(answer)