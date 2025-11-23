# https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/description/

class Solution:
    def sumZero(self, n: int) -> List[int]:
        lst = []
        i = 1

        while len(lst) < n and (n - len(lst) > 1):
            lst.append(i)
            lst.append(-i)
            i += 1
        
        if n % 2 == 1:
            lst.append(0)
            return lst
        else:
            return lst
