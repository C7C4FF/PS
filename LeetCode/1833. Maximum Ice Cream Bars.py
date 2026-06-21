# https://leetcode.com/problems/maximum-ice-cream-bars/?envType=daily-question&envId=2026-06-21
# counting sort 를 반드시 사용하기. -> 최댓값을 구하고 최댓값 + 1 길이의 배열 생성
# 그 이후에 해당 값에 맞는 위치에 그 원소가 몇번 등장했는지 표기하고 정렬하기

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        ans = 0
        largest = max(costs)
        counting = [0] * (largest + 1)

        for cost in costs:
            counting[cost] += 1

        sorted_array = []

        for i in range(len(counting)):
            sorted_array += [i] * counting[i]
        
        for num in sorted_array:
            if coins < num:
                return ans
            
            coins -= num
            ans += 1
        
        return ans
