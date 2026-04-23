# https://leetcode.com/problems/intervals-between-identical-elements/description/
# https://leetcode.com/problems/sum-of-distances/description/?envType=daily-question&envId=2026-04-23 랑 같은 문제

class Solution:
    def getDistances(self, arr: List[int]) -> List[int]:
        n = len(arr)
        ans = [0] * n

        # 인덱스 저장
        pos = defaultdict(list)
        for i in range(n):
            num = arr[i]

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
