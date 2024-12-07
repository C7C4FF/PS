# https://school.programmers.co.kr/learn/courses/30/lessons/42890

# 행렬을 미리 만들어두고 직접 돌리기...
# 2 2 5 4 -> 22 23 24 / 34 44 54 / 53 52 / 42 32

def rotation_stack(query, matrix):
    stack = []
    cur_stack = []
    x1, y1, x2, y2 = query
    
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1
    
    total = (y2-y1+1) * 2 + (x2-x1-1) * 2
    
    cur = [0, 0]
    
    cur[0] += x1
    cur[1] += y1
    
    while len(stack) != total:
        stack.append(matrix[cur[0]][cur[1]])
        cur_stack.append([cur[0], cur[1]])
        
        if len(stack) < (total // 2 + 1):
            # 우 -> 하
            if cur[1] < y2:
                cur[1] += 1
            elif cur[0] < x2:
                cur[0] += 1
        else:
            # 좌 -> 상
            if cur[1] > y1:
                cur[1] -= 1
            elif cur[0] > x1:
                cur[0] -= 1
                
    smallest = min(stack)
    stack.insert(0, stack.pop())
    
    for i in range(len(stack)):
        matrix[cur_stack[i][0]][cur_stack[i][1]] = stack[i]
    
    return smallest, matrix
    
def solution(rows, columns, queries):
    matrix = [[(columns * i) + j + 1 for j in range(columns)] for i in range(rows)]
    answer = []
    
    for query in queries:
        smallest, matrix = rotation_stack(query, matrix)
        answer.append(smallest)
        
    return answer
