# https://leetcode.com/problems/next-greater-element-i/
# Monotonic Stack, 시간복잡도 O(n)

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_greater = {}
        stack = []

        for num in nums2:
            # 현재 num이 stack의 top보다 크다면, 모든 stack[-1]에 대해 '다음 큰 원소'를 num으로 지정
            while stack and num > stack[-1]:
                prev = stack.pop()
                next_greater[prev] = num
            stack.append(num)

        # get으로 next_greater[n1] 을 가져오고, n1이 없으면 -1을 넣어주기
        return [next_greater.get(n1, -1) for n1 in nums1]


'''
# 찾아야 하는 nums2 의 n1을 먼저 찾고,
# 그 이후부터 하나씩 비교하며 더 큰 수가 나오면 break하고 해당 원소 넣기
# bruteforce.. O(n*m)

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []

        for n1 in nums1:
            idx = nums2.index(n1)
            for i in range(idx, len(nums2)):
                if n1 < nums2[i]:
                    ans.append(nums2[i])
                    break
            else:
                ans.append(-1)

        return ans
'''
