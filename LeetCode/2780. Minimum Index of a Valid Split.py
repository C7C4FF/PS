# https://leetcode.com/problems/minimum-index-of-a-valid-split/?envType=daily-question&envId=2025-03-27
# Boyer-Moore 알고리즘... 을 써도 되지만 Counter로 하면 시간복잡도를 더 줄일 수 있을듯? 해시맵이니까..

class Solution:
    '''
    def find_majority(self, lst: list[int]) -> int:
        cnt = 0
        major = 0

        for n in lst:
            if cnt == 0:
                major = n
            cnt += 1 if major == n else -1

        return major
    '''

    def minimumIndex(self, nums: List[int]) -> int:
        n = len(nums)

        # 여기에서 find_majority(nums) 로 찾고, count(majorelement) 로 몇 개인지 세도 됨
        major, freq = Counter(nums).most_common(1)[0]

        # 시간복잡도를 줄이기 위해 dominant 원소가 어디에 몇 개 있는지 저장하는 prefix 배열 생성
        prefix = [0] * (n+1)
        for i in range(n):
            prefix[i+1] = prefix[i] + (1 if nums[i] == major else 0)
        
        for i in range(1, n):
            left_cnt = prefix[i]
            right_cnt = freq - left_cnt
            
            # 왼쪽은 i개 존재, 오른쪽은 n - i개 존재
            if left_cnt * 2 > i and right_cnt * 2 > (n - i):
                return i-1

        return -1

'''
# 911/917 TLE

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            left, right = nums[:i], nums[i:]
            l_major, l_cnt = Counter(left).most_common()[0]
            r_mjaor, r_cnt = Counter(right).most_common()[0]
            
            if (l_major == r_mjaor) and (l_cnt * 2 > len(left) and r_cnt * 2 > len(right)):
                return i-1
            
        return -1
'''
