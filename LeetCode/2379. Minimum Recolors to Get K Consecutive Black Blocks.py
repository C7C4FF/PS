# https://leetcode.com/problems/minimum-recolors-to-get-k-consecutive-black-blocks/?envType=daily-question&envId=2025-03-08
# K 개씩 끊어서 확인하면서, 흰색 갯수를 검사해서 흰색이 가장 적은 서브스트링의 경우를 고르기

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        cnt = 101

        for i in range(0, len(blocks)-k+1):
            temp = blocks[i:i+k]
            cnt = min(cnt, temp.count("W"))

        return cnt
