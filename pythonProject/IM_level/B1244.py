# 스위치의 상태를 변경하는 함수
def status_change(target):
    if target == 0:
        target = 1

        return target

    elif target == 1:
        target = 0

        return target


switch_count = int(input())

switch_status = [0] + list(map(int, input().split()))

student_count = int(input())

# 학생 수만큼 반복
for i in range(student_count):
    gender, num = map(int, input().split())
    # 남자이면
    if gender == 1:
        # 스위치 전체를 순회하며
        for j in range(1, switch_count + 1):
            # 인덱스가 num의 배수이면
            if j % num == 0:
                # 스위치 상태 변경
                switch_status[j] = status_change(switch_status[j])
    # 여자이면
    elif gender == 2:
        end = 0
        # 왼쪽 끝과 오른쪽 끝 중 작은 것으로 엔드 설정
        # 스위치 수가 8이고 num이 3일 경우 왼쪽 끝으로 두 칸만 갈 수 있음
        # 스위치 수가 8이고 num이 5일 경우 오른쪽 끝으로 세 칸만 갈 수 있음
        # 더 갈 경우 인덱스 에러
        if num - 1 < switch_count - num:
            end = num - 1
        else:
            end = switch_count - num
        # 엔드 포인트 설정한 만큼 양 옆 체크
        for j in range(1, end + 1):
            # 양 옆을 비교했을 때 스위치의 상태가 같다면
            if switch_status[num - j] == switch_status[num + j]:
                # 양 옆 두 상태 비교
                switch_status[num - j] = status_change(switch_status[num - j])
                switch_status[num + j] = status_change(switch_status[num + j])
            # 다르다면 반복 종료
            else:
                break
        # 양 옆만 비교해서 상태 변경 했기 때문에 현재 위치 상태 변경
        switch_status[num] = status_change(switch_status[num])

# 스위치 수 만큼 상태 출력
for i in range(1, switch_count + 1):
    print(switch_status[i], end=' ')
    # 출력에서 한 줄에 20개 입력 후 줄 바꿈하라고 했기에
    # 20으로 나누어 떨어지면 '\n' 출력
    if i % 20 == 0:
        print()