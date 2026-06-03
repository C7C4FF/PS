# https://leetcode.com/problems/earliest-finish-time-for-land-and-water-rides-ii/?envType=daily-question&envId=2026-06-03
# 먼저 하나를 끝내고 다음 걸 계싼하기.

class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        def take_ride(start1, duration1, start2, duration2):
            n, m = len(start1), len(start2)
            first_finish = float('inf')
            final = float('inf')
            
            for i in range(n):
                first_finish = min(first_finish, start1[i] + duration1[i])
            for i in range(m):
                final = min(final, max(start2[i], first_finish) + duration2[i])

            return final

        
        land_to_water = take_ride(landStartTime, landDuration, waterStartTime, waterDuration)
        water_to_land = take_ride(waterStartTime, waterDuration, landStartTime, landDuration)

        return min(land_to_water, water_to_land)
            
            
                


        return ans
