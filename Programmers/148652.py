def solution(n, l, r):
    def count_ones(n, l, r):
        length = 5**n
        
        if n == 0:
            return 1 if l <= 1 <= r else 0
        
        prev_length = length // 5
        
        # 각 구간에 대해 계산
        count = 0
        for i in range(5):
            start = i * prev_length + 1
            end = (i + 1) * prev_length
            
            # 0 인 부분은 패스
            if i == 2:
                continue
            
            if l <= end and r >= start:
                new_l = max(l, start) - start + 1
                new_r = min(r, end) - start + 1
                # 재귀
                count += count_ones(n - 1, new_l, new_r)
        
        return count
    
    return count_ones(n, l, r)

```
3문제 시간 초과..

def chk_bit(position, n):
    """
    특정 위치가 n번째 비트열에서
    1인지 0인지 확인하는 함수
    """
    while n > 0:
        length = 5**(n-1)
        section = (position - 1) // length 
        if section == 2:  # 세 번째 구간은 0
            return 0
        position = (position - 1) % length + 1
        n -= 1
        
    return 1

def solution(n, l, r):
    count = 0
    
    for i in range(l, r + 1):
        count += chk_bit(i, n)

    return count

# 1 -> 1 - 1
# 11011 -> 5 - 4
# 11011 / 11011 / 00000 / 11011 / 11011 -> 25 - 16
# 125 - 16*4

```
