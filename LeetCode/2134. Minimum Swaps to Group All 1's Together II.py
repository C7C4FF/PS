# https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/
# circular 한 특성은 처음만 검사하면 x..
#     -> 뒤에 윈도우 크기만큼 붙여주기.
#     -> 혹은 길이로 나눠준 나머지를 검사할 수도 있음. 
#        circular[i+one-1] 대신에 nums[(i + one - 1) % n] 로...
#
# count(0) 을 하면 매번 O(n) 시간복잡도 발생 -> 시간초과
# 대신 윈도우를 옮길 때마다 나가는 0과 들어오는 0을 검사

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        one = sum(nums)

        circular = nums + nums

        # 첫 윈도우의 0의 갯수
        cnt = one - sum(nums[:one])
        # 각 윈도우를 돌면서 사용할 0의 갯수
        now = cnt

        if cnt == one:
            return 0
        else:
            for i in range(1, len(nums)+1):
                if circular[i-1] == 0:
                    now -= 1

                if circular[i+one-1] == 0:
                    now += 1

                cnt = min(now, cnt)

        return cnt


'''
시간 초과...

class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        one = nums.count(1)
        cnt = 10**5
        
        circular = nums + nums

        for i in range(0, len(nums)):
            temp = circular[i:i+one]
            cnt = min(cnt, temp.count(0))

        return cnt
'''
