# https://school.programmers.co.kr/learn/courses/30/lessons/12904
# 투포인터 풀이, https://github.com/C7C4FF/PS/blob/main/LeetCode/5.%20Longest%20Palindromic%20Substring.py 

def solution(s):
    answer = ''

    def expand(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            
        return s[left+1:right]
    
    if len(s) == 1 or s == s[::-1]:
        return len(s)
    
    for i in range(len(s) - 1):
        answer = max(answer, expand(i, i+1), expand(i, i+2), key=len)
    
    return len(answer)
