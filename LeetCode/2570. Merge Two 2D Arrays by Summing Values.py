# https://leetcode.com/problems/merge-two-2d-arrays-by-summing-values/?envType=daily-question&envId=2025-03-02

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        pairs = defaultdict(int)
        
        for k, v in nums1:
            pairs[k] += v
        for k, v in nums2:
            pairs[k] += v

        return sorted([[k, v] for k, v in pairs.items()])


'''
class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        pairs = defaultdict(int)
        
        length = max(len(nums1), len(nums2))

        for i in range(length):
            try:
                pairs[nums1[i][0]] += nums1[i][1]
            except:
                pass
            
            try:
                pairs[nums2[i][0]] += nums2[i][1]
            except:
                pass

        ans = sorted([[k, v] for k, v in pairs.items()])

        return ans
'''
