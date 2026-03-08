# https://leetcode.com/problems/find-unique-binary-string/editorial/?envType=daily-question&envId=2026-03-08
# 칸토어의 대각선 논법 대신 모든 조합을 만들어서 사용하기

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)

        c = list(product([0, 1], repeat = n))
        
        for binary in c:
            target = "".join(map(str, binary))
            if target not in nums:
                return target
                
'''
# https://leetcode.com/problems/find-unique-binary-string/?envType=daily-question&envId=2025-02-20
# n == nums.length.. 현재 주어진 nums의 원소에서 각 자리의 수를 다르게 하면
# nums 리스트 안의 모든 수에서 하나씩은 차이나게 됨...

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        answer = ''

        for i in range(len(nums)):
            if nums[i][i] == '0':
                answer += '1'
            else:
                answer += '0'

        return answer
'''
