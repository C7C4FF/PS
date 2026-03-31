# https://leetcode.com/problems/candy/description/

# 정방향으로 가면서 체크하기. 크면 그것보다 + 1 씩 해주기.
# 역방향으로 가면서 다시 체크하기. 

class Solution:
    def candy(self, ratings: List[int]) -> int:
        candies = [1] * len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i-1] > ratings[i]:
                if candies[i-1] <= candies[i]:
                    candies[i-1] = candies[i] + 1
            elif ratings[i-1] < ratings[i]:
                if candies[i] <= candies[i-1]:
                    candies[i] = candies[i-1] + 1
                    
        for i in range(len(ratings)-1, 0, -1):
            if ratings[i-1] > ratings[i]:
                if candies[i-1] <= candies[i]:
                    candies[i-1] = candies[i] + 1
            elif ratings[i-1] < ratings[i]:
                if candies[i] <= candies[i-1]:
                    candies[i] = candies[i-1] + 1

        return sum(candies)
