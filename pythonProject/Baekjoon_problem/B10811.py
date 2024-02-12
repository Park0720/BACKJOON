N, M = map(int, input().split())
basket_list = list(range(1, N+1))
for _ in range(M):
    i, j = map(int, input().split())
    basket_list[i-1:j] = basket_list[i-1:j][::-1]


print(*basket_list)