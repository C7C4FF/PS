# https://school.programmers.co.kr/learn/courses/30/lessons/49994

def check(x, y):
    if x < -5:
        x = -5
    elif x > 5:
        x = 5
    if y < -5:
        y = -5
    elif y > 5:
        y = 5
    
    return x, y

def solution(dirs):
    x, y = 0, 0
    
    #     좌 우 하 상
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    path = set()
    
    for d in dirs:
        if d == "L":
            nx, ny = x + dx[0], y + dy[0]
            nx, ny = check(nx, ny)
        elif d == "R":
            nx, ny = x + dx[1], y + dy[1]
            nx, ny = check(nx, ny)
        elif d == "D":
            nx, ny = x + dx[2], y + dy[2]
            nx, ny = check(nx, ny)
        elif d == "U":
            nx, ny = x + dx[3], y + dy[3]
            nx, ny = check(nx, ny)

        # 이전과 같은 좌표를 가졌다면 (가장자리에 부딪혔다면) 패스
        if x == nx and y == ny:
            pass
        else:
            # 역방향이 있다면 패스
            if (nx, ny, x, y) in path:
                pass
            else:
                path.add((x, y, nx, ny))
                
        x, y = nx, ny
        
    return len(path)
