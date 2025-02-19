# https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/?envType=daily-question&envId=2025-02-19
# 총 수는 3 * 2^(n-1) . 첫번째에는 abc 전부 가능하고, 그 이후부터는 이전의 값을 뺀 두가지씩 반복... 

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        lst = ['a', 'b', 'c']
        answer = ''

        total = 3 * (2 ** (n-1))
        if k > total:
            return ""
        
        k -= 1
        if n == 1:
            return lst[k]
        
        std = 2 ** (n - 1)
        first = k // std
        answer += lst[first]
        k %= std
        
        # 매 선택마다 2가지 경우가 가능하기 때문에
        # 2씩 나눈 몫으로 순서를 결정해서 문자에 추가
        for i in range(1, n):
            std = 2 ** (n - 1 - i)
            q = k // std
            k %= std
            
            possible = [ch for ch in lst if ch != answer[-1]]
            answer += possible[q]
                    

        return answer            
        
