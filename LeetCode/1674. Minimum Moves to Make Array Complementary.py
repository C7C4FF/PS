# https://leetcode.com/problems/minimum-moves-to-make-array-complementary/?envType=daily-question&envId=2026-05-13

# 한 쌍의 a, b 가 있을 때. 이 합을 X 로 만들기 위해서는

# 0번 교체 a+b = X
# 1번 교체 min(a, b) + 1 <= X <= max(a, b) + limit 
# 2번 교체 1 <= X <= limit * 2

class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        
        left, right = nums[:n//2], nums[::-1][:n//2]
        diff = [0] * (limit * 2 + 2)    # 목표 X 가 되기 위해서 몇번 움직임이 필요한지 누적합으로 계산해야 함

        for i in range(len(left)):
            diff[2] += 2
            # 일단 모두 2번씩 움직인다고 가정
            
            diff[min(left[i], right[i]) + 1] -= 1
            # 숫자 하나만 바꿔도 되는 수의 시작점

            diff[left[i] + right[i]] -= 1
            # 숫자를 아무것도 바꾸지 않아도 됨. min(a, b) + 1 에서 1을 뺐으니 또 1을 빼줌 > 도합 0번 이동
            
            diff[left[i] + right[i] + 1] += 1
            # 아무것도 바꾸지 않아도 되는 부분을 지났으면 다시 1씩 이동해야 함

            diff[max(left[i], right[i]) + limit + 1] += 1
            # 숫자 하나만 바꿔도 되는 수의 끝 점

        ans = []
        prefix_sum = 0
        for X in range(2, 2 * limit + 1):
            prefix_sum += diff[X]
            ans.append(prefix_sum)

        return min(ans)
