# https://leetcode.com/problems/sum-of-distances/description/?envType=daily-question&envId=2026-04-23

# (pos[num][i] - pos[num][0]) + ... + (pos[num][i] - pos[num][i-1]) + (pos[num][i+1] - pos[num][i]) + ... + (pos[num][n-1] - pos[num][i])
# pos[num][i] * i - (pos[num][0] + [1] + ... + [i-1]) + (pos[num][i+1] + [i+2] + ... + [n-1]) - pos[num][i] * (n-i-1)
# => ans[idx] = (total - idx * length) - 2 * (current_sum - idx * (i + 1))

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n

        # 인덱스 저장
        pos = defaultdict(list)
        for i in range(n):
            num = nums[i]

            pos[num].append(i)
        
        for num, indices in pos.items():
            length = len(indices)
            if length == 1:
                continue

            total = sum(indices)    # 전체 누적합
            current_sum = 0         # 현재 인덱스를 포함한 누적합

            for i in range(length):
                idx = indices[i]

                current_sum += idx
                ans[idx] = (total - idx * length) - 2 * (current_sum - idx * (i + 1))


        return ans
