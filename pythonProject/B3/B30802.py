N = int(input())

size_list = list(map(int, (input().split())))

T, P = map(int, input().split())

t_shirt = 0

for size in size_list:
    t_shirt += (size - 1) // T + 1

pen_bundle, pen_each = N // P, N % P

print(t_shirt)

print(pen_bundle, pen_each)
