# https://leetcode.com/problems/partition-labels/?envType=daily-question&envId=2025-03-30

# 주어진 문자열을 자르되, 나눠진 각 부분에 있는 한 글자는 다른 부분에서 등장하면 안 됨
# 해당 조건을 만족하는 부분들의 길이를 리스트로 반환

# s 를 한번 돌면서 특정 문자가 가장 마지막에 나온 index 를 저장
# 문자열을 다시 돌면서 포함되는 문자들의 '마지막에 나온 index'를 최신화
# 더 이상의 최신화 없이 해당 index에 도착했다면, 문자열 길이 저장

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_occur = defaultdict(int)
        
        for i in range(len(s)):
            last_occur[s[i]] = i

        ans = []
        start, end = 0, 0

        for i in range(len(s)):
            end = max(end, last_occur[s[i]])

            if i == end:
                ans.append(i - start + 1)
                start = i + 1
        
        return ans

        
            
        
