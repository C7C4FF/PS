# https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-i/?envType=daily-question&envId=2026-06-02
# 브루트포스..

class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        n, m = len(landStartTime), len(waterStartTime)
        ans = float('inf')

        for i in range(n):
            for j in range(m):
                land = landStartTime[i] + landDuration[i]
                water = waterStartTime[j] + waterDuration[j]

                # 1. land ride 를 타고도 water ride 가 시작하지 않았다면 기다렸다가 water ride 타기
                # 2. land ride 를 타는 중간에 water ride 가 시작됐다면, 끝난 이후 바로 시작하기
                if land < waterStartTime[j]:
                    ans = min(ans, water)
                else:
                    ans = min(ans, land + waterDuration[j])

                # 3. water ride 가 끝나고도 land ride가 시작하지 않았다면 기다렸다가 land ride 타기
                # 4. water ride 도중 land ride 가 시작됐다면, 끝난 이후 바로 시작하기
                if water < landStartTime[i]:
                    ans = min(ans, land)
                else:
                    ans = min(ans, water + landDuration[i])
            
                


        return ans
