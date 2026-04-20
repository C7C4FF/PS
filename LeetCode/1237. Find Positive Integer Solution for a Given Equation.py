# https://leetcode.com/problems/find-positive-integer-solution-for-a-given-equation/description/
# binary search를 사용할 수 있는 이유: monotoically increasing 이라고 명시되어 있기 때문
# f(x, y) < f(x+1, y) & f(x, y) < f(x, y+1) : x도 y도 오름차순으로 정렬되어 있다는 뜻

"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        ans = []

        for x in range(1, 1001):
            low, high = 1, 1000

            while low <= high:
                mid = (low + high) // 2

                if customfunction.f(x, mid) == z:
                    ans.append([x, mid])
                    break
                elif customfunction.f(x, mid) > z:
                    high = mid - 1
                else:
                    low = mid + 1

        return ans

'''
class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        ans = []
        
        for x in range(1, 1001):
            for y in range(1, 1001):
                if customfunction.f(x, y) == z:
                    ans.append([x, y])

        return ans
'''
