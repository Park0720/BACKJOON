def pre_order(node):
    if node == '.':
        return

    print(chr(adjl[node][0] + 65), end='')
    pre_order(adjl[node][1])
    pre_order(adjl[node][2])


def in_order(node):
    if node == '.':
        return

    in_order(adjl[node][1])
    print(chr(adjl[node][0] + 65), end='')
    in_order(adjl[node][2])


def post_order(node):
    if node == '.':
        return

    post_order(adjl[node][1])
    post_order(adjl[node][2])
    print(chr(adjl[node][0] + 65), end='')


N = int(input())

adjl = []

for i in range(N):
    input_list = list(map(str, input().split()))
    adjl.append(input_list)

for i in range(N):
    adjl[i] = list(map(ord, adjl[i]))
    for j in range(len(adjl[i])):
        adjl[i][j] -= 65
        if adjl[i][j] < 0:
            adjl[i][j] = '.'

adjl.sort(key= lambda x: x[0])
pre_order(0)
print()
in_order(0)
print()
post_order(0)