# https://leetcode.com/problems/letter-tile-possibilities/?envType=daily-question&envId=2025-02-17
# 순열의 중복 문제를 집합으로 처리하고, 그 갯수만 계산해서 반환하기.
# 백트래킹으로도 가능..

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        cnt = 0

        for i in range(1, len(tiles)+1):
            temp = set(permutations(tiles, i))
            cnt += len(temp)
        
        return cnt
