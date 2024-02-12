# # Ver.1
#
# width, height = map(int, input().split())
#
# base_list = [[0] * width for _ in range(height)]
#
# N = int(input())
#
# x_list = [0]
# y_list = [0]
#
# for i in range(N):
#     mode, point = map(int, input().split())
#     if not mode:
#         x_list.append(point)
#     else:
#         y_list.append(point)
#
# x_list.sort()
# y_list.sort()
#
# x_list.append(height)
# y_list.append(width)
#
# _max = 0
# for i in range(len(x_list)-1):
#     for j in range(len(y_list)-1):
#         count = 0
#         for m in range(x_list[i], x_list[i+1]):
#             for n in range(y_list[j], y_list[j+1]):
#                 count += 1
#         if count > _max:
#             _max = count
#
# print(_max)

# Ver.2

width, height = map(int, input().split())

base_list = [[0] * width for _ in range(height)]

N = int(input())

x_list = [0]
y_list = [0]

for i in range(N):
    mode, point = map(int, input().split())
    if not mode:
        x_list.append(point)
    else:
        y_list.append(point)

x_list.sort()
y_list.sort()

x_list.append(height)
y_list.append(width)

x_max = 0
y_max = 0
for i in range(len(x_list) - 1):
    val = x_list[i+1] - x_list[i]
    if val > x_max:
        x_max = val
for j in range(len(y_list) - 1):
    val = y_list[j+1] - y_list[j]
    if val > y_max:
        y_max = val

print(x_max * y_max)