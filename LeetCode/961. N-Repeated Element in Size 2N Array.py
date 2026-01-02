# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/

# defaultdict 로 세어보기 연습..
# 외에도 return Counter(nums).most_common()[0][0],
# n+1 개의 unique elements 존재. 한 원소가 n번 반복된다면, 다른 원소들은 1번밖에 존재할 수 없음.
#   -> 집합으로 표현할 수 있음
#       seen = set(), element in seen -> return element

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums) // 2
        pos = defaultdict(list)
        for i, v in enumerate(nums):
            pos[v].append(i)

        for v, lst in pos.items():
            if len(lst) == n:
                return v
'''
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        temp = []
        for i in range(len(nums)):
            if nums[i] in temp:
                return nums[i]
            else:
                temp.append(nums[i])
#####
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        return Counter(nums).most_common()[0][0]
'''
