def solution(m, n, startX, startY, balls):
    answer = []
    
    for x, y in balls:
        up, down, left, right = 2147483647, 2147483647, 2147483647, 2147483647
        
        # 위로 쿠션, y좌표를 y = n에 대하여 대칭이동
        up = (startX - x) ** 2 + (startY - (n + (n - y))) ** 2
        
        # 아래로 쿠션, y좌표를 y = 0에 대하여 대칭이동
        down = (startX - x) ** 2 + (startY - (-y)) ** 2
        
        # 왼쪽 쿠션, x좌표를 0에 대하여 대칭이동
        left = (startX - (-x)) ** 2 + (startY - y) ** 2
        
        # 오른쪽 쿠션, x좌표를 x = m에 대하여 대칭이동
        right = (startX - (m + (m - x))) ** 2 + (startY - y) ** 2

        # 수직선 상에 있을 경우
        if startX == x:
            # 아래로 치면 원쿠션이 안 됨
            if startY > y:
                down = 2147483647
            # 위로 치면 원쿠션이 안 됨
            else:
                up = 2147483647

        # 수평선 상에 있을 경우
        if startY == y:
            # 왼쪽으로 치면 원쿠션이 안 됨
            if startX > x:
                left = 2147483647
            # 오른쪽으로 치면 원쿠션이 안 됨
            else:
                right = 2147483647
                
        answer.append(min(up, down, left, right))

    return answer
