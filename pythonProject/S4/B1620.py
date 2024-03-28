import sys

N, M = map(int, sys.stdin.readline().split())

# 이름과 번호 매핑을 저장할 딕셔너리 생성
name_to_number = {}
number_to_name = {}

# 이름과 번호를 읽고 저장
for i in range(1, N+1):
    name = sys.stdin.readline().strip()
    name_to_number[name] = str(i)
    number_to_name[str(i)] = name


# 쿼리를 처리하는 함수
def process_query(query):
    if query.isdigit():
        print(number_to_name[query])
    else:
        print(name_to_number[query])


# 쿼리를 읽고 처리
for i in range(M):
    problem = sys.stdin.readline().strip()
    process_query(problem)
