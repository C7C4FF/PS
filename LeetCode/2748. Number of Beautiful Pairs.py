# https://leetcode.com/problems/number-of-beautiful-pairs/description/
# coprime = 서로소, 둘의 공통 약수가 1인 수
# 첫번째 자리, 마지막 자리를 구하기 위해서 숫자를 문자로 바꾸고 각각 인덱스를 넣어주기

class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if math.gcd(int(str(nums[i])[0]), int(str(nums[j])[-1])) == 1:
                    ans += 1

        return ans
