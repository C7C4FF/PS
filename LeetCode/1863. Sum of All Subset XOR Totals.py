# https://leetcode.com/problems/sum-of-all-subset-xor-totals/?envType=daily-question&envId=2025-04-05
# 시간 복잡도 생각 안 하고, 미리 부분집합 모두 만들기 -> xor 계산
# 순회하되 generator 로 만들기. reduce, operator 의 xor 라이브러리로 계산하기

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        lst = chain.from_iterable(combinations(nums, r) for r in range(len(nums) + 1))

        cnt = 0
        for subset in lst:
            cnt += reduce(xor, subset, 0)

        '''
        for subset in lst:
            temp = 0
            for number in subset:
                temp ^= number
            cnt += temp
        '''

        return cnt

'''
# 생각 못했을 방법...
# i 번째 비트가 홀수번 나타나면 1, 짝수번 나타나면 0이 됨
# 배열의 모든 부분집합의 수는 2^n 개. 특정 원소 하나를 포함하는 부분집합은 2^(n-1)개.

# i 번째 비트가 1인 원소가 m개 있으면, 해당 원소들 중에 홀수 개를 고르는 방법은 2^(m-1).
# i 번째 비트가 0인 원소는 (n-m)개, 이 원소는 선택되어도, 되지 않아도 상관 x. 2^(n-m)
# i 번째 비트에게 영향을 주는 식은 결국 2^(m-1) * 2^(n-m) = 2^(n-1)

# 그래서 |= 으로 해당 비트가 얼마나 기여했는지를 확인하고, << 연산으로 2^(n-1) 연산 수행........

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans = 0
        for i in nums:
            ans |= i
        return ans << (len(nums)-1)
'''
