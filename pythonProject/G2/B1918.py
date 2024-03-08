T = 10

infix = input()
N = len(infix)
top = -1
stack = [0] * (N + 1)

icp = {'(': 3, '*': 2, '/': 2, '+': 1, '-': 1, 0: -1}  # 스택 밖에서의 우선순위
isp = {'(': 0, '*': 2, '/': 2, '+': 1, '-': 1, 0: -1}  # 스택 안에서의 우선순위

postfix = ''
for token in infix:
    # 여는 괄호이면 push, 연산자이고 top 원소보다 우선순위가 높으면 push
    if token == '(' or (token in '*/+-' and isp[stack[top]] < icp[token]):
        # push
        top += 1
        stack[top] = token
    # 연산자이고 top 원소보다 우선순위가 높지 않으면
    elif token in '*/+-' and isp[stack[top]] >= icp[token]:
        # top 원소의 우선순위가 낮을 때까지 pop
        while isp[stack[top]] >= icp[token]:
            top -= 1
            postfix += stack[top + 1]
        top += 1
        stack[top] = token
    # 닫는 괄호면, 여는 괄호를 만날때까지 pop
    elif token == ')':
        while stack[top] != '(':
            top -= 1
            postfix += stack[top + 1]
        # 여는 괄호 pop 해서 버려줌
        top -= 1
        stack[top + 1]
    # 피연산자인 경우
    else:
        postfix += token

while top > -1:
    postfix += stack[top]
    top -= 1

print(postfix)