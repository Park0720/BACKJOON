import sys
import heapq as hq

input = sys.stdin.readline


T = int(input())
for _ in range(T):
    n = int(input())
    min_queue = []
    max_queue = []
    hq.heapify(min_queue)
    hq.heapify(max_queue)
    del_list = {}
    vaild = 0 # 힙에 남아있는 원소 수
    for _ in range(n):
        txt, num = input().rstrip().split()
        num = int(num)
        if txt == "I":
            hq.heappush(min_queue, num)
            hq.heappush(max_queue, -num)
            if num in del_list:
                del_list[num] += 1 # 해당 번호를 방문해야함
            else:
                del_list[num] = 1

            vaild += 1 # 힙에 추가된 원소 수
        elif txt == "D":
            if num == -1:
                while min_queue:
                    del_num = hq.heappop(min_queue)
                    if del_num in del_list and del_list[del_num] > 0:
                        del_list[del_num] -= 1 # 해당 번호 방문 처리
                        vaild -= 1 # pop한 원소 빼기
                        break

            elif num == 1:
                while max_queue:
                    del_num = -hq.heappop(max_queue)
                    if del_num in del_list and del_list[del_num] > 0:
                        del_list[del_num] -= 1 # 해당 번호 방문처리
                        vaild -= 1 # pop한 원소 빼기
                        break

    if vaild > 0 : # 원소 수가 남아있다면
        while True:
            min_ = hq.heappop(min_queue)
            if min_ in del_list and del_list[min_] > 0: # 힙 안에 남아있으면서 가장 작은 값
                break
        while True:
            max_ = -hq.heappop(max_queue)
            if max_ in del_list and del_list[max_] > 0: # 힙 안에 남아있으면서 가장 큰 값
                break
        print(max_, min_)
    else:
        print("EMPTY")