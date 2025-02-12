# https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/?envType=daily-question&envId=2025-02-12
# map 으로 숫자들을 문자로 바꾸고, 모든 자리 숫자의 합으로 해시맵을 만듦.
#   % 10 을 반복해서 while 문으로도 가능 
# 그 중 2개 이상인 것에 한해서 최댓값 구하기


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        answer = -1
        
        nums_sum = [list(map(int, str(num))) for num in nums]
        nums_hash = defaultdict(list)

        for i in range(len(nums_sum)):
            temp = sum(nums_sum[i])
            nums_hash[temp].append(nums[i])
        
        for i in nums_hash:
            if len(nums_hash[i]) >= 2:
                answer = max(answer, sum(heapq.nlargest(2, nums_hash[i])))
        

        return answer
