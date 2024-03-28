import sys

sys.setrecursionlimit(10 ** 6)


def pre_to_post(start, end):
    # 시작 인덱스가 끝 인덱스 보다 크면 종료
    if start > end:
        return

    # 현재 서브트리의 루트 노드
    root = pre_order_list[start]
    idx = start + 1

    while idx <= end:
        # 루트보다 큰 값이 나오면 오른쪽 자식 노드(이진 검색트리)
        if pre_order_list[idx] > root:
            break
        idx += 1

    # 왼쪽 서브트리 후위순회
    pre_to_post(start + 1, idx - 1)
    # 오른쪽 서브트리 후위순회
    pre_to_post(idx, end)
    # 후위순회이므로 현재 루트노드 마지막에 출력
    print(root)


pre_order_list = []
while True:
    try:
        pre_order_list.append(int(input()))
    except:
        break

in_order_list = sorted(pre_order_list)

pre_to_post(0, len(pre_order_list) - 1)
