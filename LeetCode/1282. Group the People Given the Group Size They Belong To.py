# https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/description/

# value: 그룹의 크기. 그룹의 크기별로 정렬해서 순서대로 자리에 넣기
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        ans = []
        min_heap = []

        for idx, value in enumerate(groupSizes):
            heapq.heappush(min_heap, (value, idx))

        while min_heap:
            value, idx = heapq.heappop(min_heap)
            attendant = [idx]
            if value > 1:
                for i in range(value-1):
                    v, i = heapq.heappop(min_heap)
                    attendant.append(i)
            ans.append(attendant)
        
        return ans
