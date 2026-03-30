# https://leetcode.com/problems/longest-subsequence-with-limited-sum/
# subSequence -> sorting, accumulatedSum -> prefixSum, closestSum -> binarySearch

# 정렬하고 가장 낮은 수부터 더해가며 찾기

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n, m = len(nums), len(queries)
        nums.sort()
        ans = []

        for query in queries:
            temp = 0
            for i in range(n):
                temp += nums[i]
                if temp <= query:
                    if i == n-1:
                        ans.append(n)
                    else:
                        continue
                else:
                    ans.append(i)
                    break

        return ans
            
