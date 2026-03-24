# https://leetcode.com/problems/min-stack/description/
# 스택을 구현하는데 스택을 쓰는 게 맞나 . . .

class MinStack:

    def __init__(self):
        self.minimum = []
        self.stack = []

    def push(self, val: int) -> None:
    # 현재 들어온 최솟값보다 작은 경우에만 저장 > 그 외에는 나가도 순서에 상관 없음
        self.stack.append(val)
        if not self.minimum or val <= self.minimum[-1]:
            self.minimum.append(val)

    def pop(self) -> None:
        if self.stack.pop() == self.minimum[-1]:
            self.minimum.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
