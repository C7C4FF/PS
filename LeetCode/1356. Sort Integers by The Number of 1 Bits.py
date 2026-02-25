# https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/?envType=daily-question&envId=2026-02-25
# 10^4 는 10000 > 최대 1이 13개까지 있을 수 있음
# sum(list, []) -> 리스트끼리 더하면 리스트 결합이 됨, 비우면 기본값이 0이기 때문에 빈 리스트를 줘야 함
# 리스트 컨프리헨션으로 할 수도 있음. [x for sublst in lst for x in sublst]

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        lst = [[] for _ in range(14)]

        arr.sort()
        
        for n in arr:
            target = bin(n)[2:]
            ones = int(target.count('1'))
            lst[ones].append(n)

        return sum(lst, [])


        
