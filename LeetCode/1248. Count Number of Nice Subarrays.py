class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        answer = t = 0
        cnt = Counter({0: 1})
        
        for v in nums:
            t += v & 1
            answer += cnt[t - k]
            cnt[t] += 1
        
        return answer
