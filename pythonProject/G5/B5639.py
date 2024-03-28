import sys
sys.setrecursionlimit(10**6)


def pre_to_post(start, end):
    if start > end:
        return

    root = pre_order_list[start]
    idx = start + 1

    while idx <= end:
        if pre_order_list[idx] > root:
            break
        idx += 1

    pre_to_post(start+1, idx-1)
    pre_to_post(idx, end)
    print(root)


pre_order_list = []
while True:
    try:
        pre_order_list.append(int(input()))
    except:
        break

in_order_list = sorted(pre_order_list)

pre_to_post(0, len(pre_order_list)-1)
