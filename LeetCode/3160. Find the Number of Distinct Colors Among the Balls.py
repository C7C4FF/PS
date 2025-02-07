# https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/description/?envType=daily-question&envId=2025-02-07

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        cnt = Counter()
        ball = {}
        answer = []

        for pos, color in queries:
            if pos in ball:
                previous = ball[pos]
                cnt[previous] -= 1

                if cnt[previous] == 0:
                    del cnt[previous]
                
            ball[pos] = color
            cnt[color] += 1
            answer.append(len(cnt))

        return answer
