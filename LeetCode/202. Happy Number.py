# https://leetcode.com/problems/happy-number/description
# seen 에 있는 수로 돌아왔다면 사이클이 만들어진 것 > False 반환

class Solution:
    def isHappy(self, n: int) -> bool:
        for i in range(60):
            if n == 1:
                return True

            lst = list(str(n))
            temp = 0
            
            for num in lst:
                temp += int(num)**2
            
            n = temp

        return False

'''

class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            s = 0
            while n > 0:
                n, d = divmod(n, 10)
                s += d ** 2
            n = s
        return n == 1
'''

            
