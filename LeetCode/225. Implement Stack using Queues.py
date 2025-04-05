# https://leetcode.com/problems/implement-stack-using-queues/
# 파이썬에서는 리스트 자료형에서 가능한 것들로만 써도 풀리긴 함...
# 그치만 문제에서 주어진 조건은 큐를 사용해서 만들어라.

class MyStack:

    def __init__(self):
        self.q = collections.deque()

    def push(self, x: int) -> None:
        ''' 스택은 LIFO 구조. 마지막에 넣은 게 맨 처음에 나오도록 함'''
        self.q.append(x)
        # 요소 삽입 후 맨 앞에 두는 상태로 재정렬
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
