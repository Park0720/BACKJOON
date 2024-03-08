def pre_order(node):
    if node <= N and node != '.':
        print(node)
        pre_order(node * 2)
        pre_order(node * 2 + 1)




N = int(input())
tree = [[0] * 3 for _ in range(N)]

for i in range(N):
    node, left, right = map(str, input().split())
    tree[i] = [node, left, right]

print(tree)
pre_order(1)
