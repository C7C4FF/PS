# https://leetcode.com/problems/jump-game/description/

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        furthest = 0

        for i in range(len(nums)):
            if i > furthest: # 가장 멀리 갈 수 있는 경우가 i에 도달할 수 없다면 False 반환
                return False
            
            furthest = max(furthest, i + nums[i]) # furthest 와 현재 인덱스 + 현재 원소 값을 비교해서 더 큰 것을 선택
            if furthest >= len(nums) - 1: # 그 값이 마지막보다 멀리 간다면 True 반환
                return True

        return False # 끝까지 가는데 실패했다면 False 반환 
