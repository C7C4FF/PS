# https://leetcode.com/problems/closest-equal-element-queries/description/?envType=daily-question&envId=2026-04-16
# 리스트 길이가 크다면 이어 붙이기보다는 모듈러 연산하기

class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        ans = []
        n = len(nums)

        seen = defaultdict(list)
        pos_seen = [0] * n
        for i in range(n):
            pos_seen[i] = len(seen[nums[i]])
            seen[nums[i]].append(i)

        for query in queries:
            target = nums[query]
            pos = seen[target]
            m = len(pos)

            if len(seen[target]) < 2:
                ans.append(-1)
            else:
                start = pos_seen[query]

                now = pos[start]
                next_idx = pos[(start+1) % m]
                prev_idx = pos[start-1]

                distance_to_next = (next_idx - now + n) % n
                distance_to_prev = (now - prev_idx + n) % n

                distance = min(distance_to_next, distance_to_prev)

                ans.append(distance)
        
        return ans
