for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())

    # 겹치지 않는 경우
    if p1 < x2 or p2 < x1 or q1 < y2 or q2 < y1:
        print('d')

    # 점에서 겹치는 경우
    elif p1 == x2 and (y1 == q2 or q1 == y2) or p2 == x1 and (y1 == q2 or q1 == y2):
        print('c')

    # 선분으로 겹치는 경우
    elif p1 == x2 or p2 == x1 or q1 == y2 or q2 == y1:
        print('b')

    # 그 외 모든 경우
    else:
        print('a')
