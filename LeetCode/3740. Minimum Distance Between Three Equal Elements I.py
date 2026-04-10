# https://leetcode.com/problems/minimum-distance-between-three-equal-elements-i/description/?envType=daily-question&envId=2026-04-10

# abs(i - j) + abs(j - k) + abs(k - i) 거리는 i > j > k 임
# 절댓값을 벗기면 j - i + k - j + k - i  -> j가 사라져서 2 * (k - i) 가 됨
# 가장 최근에 나온 값 3개로 계산하기

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        ans = float('inf')
        cnt = defaultdict(list)

        for idx, num in enumerate(nums):
            cnt[num].append(idx)

            if len(cnt[num]) >= 3:
                distance = (cnt[num][-1] - cnt[num][-3]) * 2
                ans = min(ans, distance)

        if ans == float('inf'):
            return -1
        
        return ans


'''

class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        ans = float('inf')
        cnt = defaultdict(list)

        for i in range(len(nums)):
            cnt[nums[i]] += [i]

        for k, v in cnt.items():
            if len(v) >= 3:
                for i in range(len(v)):
                    for j in range(i+1, len(v)):
                        for l in range(j+1, len(v)):
                            distance = abs(v[i] - v[j]) + abs(v[j] - v[l]) + abs(v[l] - v[i])
                            ans = min(ans, distance)

        if ans == float('inf'):
            return -1

        return ans
'''
        
        
        
