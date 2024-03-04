M, N = map(int, input().split())
prime = [True] * (N+1)
p = 2
while p * p <= N:
    if prime[p] == True:
        for i in range(p * p, N+1, p):
            prime[i] = False
    p += 1

for i in range(M, N+1):
    if i > 1 and prime[i] == True:
        print(i)

'''
1. 2부터 N까지의 모든 정수를 적습니다.
2. 아직 지워지지 않은 수 중 가장 작은 수를 찾습니다. 그 수는 소수입니다.
3. 그 소수의 배수를 모두 지웁니다.
4. 더 이상 지울 수가 없을 때까지 2와 3의 과정을 반복합니다.
'''