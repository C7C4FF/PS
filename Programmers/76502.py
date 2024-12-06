# https://school.programmers.co.kr/learn/courses/30/lessons/76502
# parenthesis, brace, bracket으로 스택을 각각 나눠도 괄호의 순서도 중요함 - "{(})"
# 그럴거면 스택을 하나만 쓰는 것이 맞겠다...

def iscorrect(s):
'''
여는 괄호는 stack에 넣고, 닫는 괄호일 때 확인하기
스택에 들어있는 괄호와 닫는 괄호의 종류가 다를 경우 False 반환
'''
    # pair = {'(': ')', '{': '}', '[': ']'}
    pair = {')': '(', '}': '{', ']': '['}
    stack = []
    
    front = '({['
    back = ')}]'
    
    for now in s:
        if now in front:
            stack.append(now)
        elif now in back:
            if stack and stack[-1] == pair[now]:
                stack.pop()
            else:
                return False
    
    if len(stack) == 0:
        return True
    else:
        return False
        

def solution(s):
'''
회전하면서 괄호가 올바른 순서로 되어 있는지 확인
'''
    answer = 0
    total = list(s)
    
    for i in range(len(s)):
        if iscorrect(total):
            answer += 1
        
        total.append(total.pop(0))
    
    return answer
