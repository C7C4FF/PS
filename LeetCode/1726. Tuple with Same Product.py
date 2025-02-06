# permutations 하고 일일이 비교하는 건 메모리 초과
# https://leetcode.com/problems/tuple-with-same-product/?envType=daily-question&envId=2025-02-06

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        answer = 0

        count = Counter()

        for i in range(len(nums)):
            for j in range(i):
                # [0] * [1] == [2] * [3] 이 나오면 같은 수를 쓰는 쌍은 총 8개가 나옴
                product = nums[i] * nums[j]
                answer += count[product] * 8
                count[product] += 1 

        return answer
        
