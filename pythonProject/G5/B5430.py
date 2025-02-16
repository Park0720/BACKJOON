import sys
from collections import deque

input = sys.stdin.readline

T = int(input().strip())

for _ in range(T):
    p = input().strip()
    n = int(input().strip())
    text = input().strip()

    # 입력된 배열을 deque로 변환
    if text == "[]":
        test_list = deque()
    else:
        test_list = deque(map(int, text[1:-1].split(',')))

    reverse_flag = False  # 뒤집혔는지 여부
    error_flag = False  # 에러 발생 여부

    for type in p:
        if type == 'R':
            reverse_flag = not reverse_flag  # 뒤집기 상태만 토글
        elif type == 'D':
            if not test_list:
                print("error")
                error_flag = True
                break
            if reverse_flag:
                test_list.pop()  # 뒤집힌 상태라면 pop() (오른쪽에서 제거)
            else:
                test_list.popleft()  # 정방향이라면 popleft() (왼쪽에서 제거)

    if not error_flag:
        if reverse_flag:
            test_list.reverse()  # 최종적으로 한 번만 뒤집기

        print("[" + ",".join(map(str, test_list)) + "]")
