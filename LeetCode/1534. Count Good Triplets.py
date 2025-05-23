# https://leetcode.com/problems/count-good-triplets/description/?envType=daily-question&envId=2025-04-14

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        cnt = 0
        n = len(arr)

        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if (
                        abs(arr[i] - arr[j]) <= a and
                        abs(arr[j] - arr[k]) <= b and
                        abs(arr[i] - arr[k]) <= c
                        ):
                        cnt += 1

        return cnt
