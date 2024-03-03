w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

w_list = []
h_list = []

# 개미는 0 ~ w, 0 ~ h 사이 좌표만 움직임
for i in range(w):
    w_list.append(i)
for i in range(w, 0, -1):
    w_list.append(i)

for i in range(h):
    h_list.append(i)
for i in range(h, 0, -1):
    h_list.append(i)

# 총 움직인 거리를 리스트의 길이 2배로 나눈 나머지가 정답
x, y = w_list[(p+t) % (2*w)], h_list[(q+t) % (2*h)]

print(x, y)