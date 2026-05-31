# https://leetcode.com/problems/destroying-asteroids/?envType=daily-question&envId=2026-05-31
# 가장 작은 것부터 하나씩 파괴하면서 몸집 불리기

class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()

        for aster in asteroids:
            if mass >= aster:
                mass += aster
            else:
                return False
        
        return True
