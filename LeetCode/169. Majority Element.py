# https://leetcode.com/problems/majority-element/description/
# Boyer-Moore majority vote algorithm
# 과반이 넘는다는 것이 보장된다면 과반이 넘는 해당 원소를 선형 시간 내에 반환할 수 있음.
# 같은 수가 나올 때마다 cnt += 1, 다른 수가 나올 때마다 cnt -= 1. 음수가 되면 major를 교체

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        major = 0
        for n in nums:
            if cnt == 0:
                major = n
            if major == n:
                cnt += 1
            else:
                cnt -= 1

        return major
