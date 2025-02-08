# https://leetcode.com/problems/design-a-number-container-system/solutions/?envType=daily-question&envId=2025-02-08
# https://leetcode.com/problems/design-a-number-container-system/solutions/6391312/python-min-heap-o-log-n-o-k-log-n-o-n-beats-100/?envType=daily-question&envId=2025-02-08 참고...

# ["NumberContainers","find","change","change","change","change","find","change","find"]
# [],                   [10],[2,10],  [1,10],   [3,10],  [5,10],  [10],   [1,20], [10]
# [null,                 -1,  null,   null,      null,    null,    1,     null,    2]
# find는 가장 작은 인덱스 or -1을 반환해야 함

class NumberContainers:
    def __init__(self):
        # 숫자를 key로, 그 숫자에 해당하는 인덱스들이 들어있는 최소 힙을 value로 가진 딕셔너리
        self.num = {}
        # 인덱스를 key로, 인덱스에 해당하는 숫자가 value
        self.idx = {}

    def change(self, index: int, number: int) -> None:
        self.idx[index] = number

        if number not in self.num:
            self.num[number] = []
        heappush(self.num[number], index)


    def find(self, number: int) -> int:
        # 번호가 없다면 -1 리턴
        if number not in self.num:
            return -1
        
        
        while self.num[number]:
            # 최소 힙의 첫번째. 가장 작은 인덱스를 확인함
            min_idx = self.num[number][0]

            # 가장 작은 값, 가장 작은 인덱스의 값이 number와 동일한지 확인
            if self.idx[min_idx] == number:
                return min_idx
            
            # 그렇지 않다면 change로 바뀌었음. pop으로 해당 데이터를 제거
            heappop(self.num[number])
        
        return -1

      
# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
