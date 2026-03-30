# https://leetcode.com/problems/longest-subsequence-with-limited-sum/
# subSequence -> sorting, accumulatedSum -> prefixSum, closestSum -> binarySearch

# 누적합을 먼저 만들고, 누적합이 쿼리보다 크다면 인덱스 만큼 넣기.
# 0-indexed 라서, 그보다 작은 길이는 i로 넣으면 됨

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n, m = len(nums), len(queries)
        nums.sort()
        ans = []

        prefix = []
        temp = 0
        for num in nums:
            temp += num
            prefix.append(temp)

        for query in queries:
            for i in range(len(prefix)):
                if prefix[i] > query:
                    ans.append(i)
                    break

                if i == n-1:
                    ans.append(n)
            
        return ans

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
            
