# https://leetcode.com/problems/find-median-from-data-stream/description/
# 절반으로 나눠서 median 보다 큰 쪽을 min_heap 에, 작은 쪽을 max_heap에 두기
# max_heap = min_heap 과 길이가 같거나 1개 더 많음
# 1. 단 max_heap에 넣고, max_heap에서 가장 큰 값을 min_heap 에 넣음 (중간보다 크다면 어차피 min_heap로 돌아감)
# 2. 길이를 체크해서 min_heap에 원소가 더 많다면 다시 1개를 max_heap으로 옮겨주기

class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.max_heap, -num)
        heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))

        if len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap): # 짝수개
            return (self.min_heap[0] - self.max_heap[0]) / 2
        else: # 홀수개
            return -self.max_heap[0]
            


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
