# https://school.programmers.co.kr/learn/courses/30/lessons/131704
# order를 착각하지 말기. [4, 3, 1, 2, 5]는 첫번째로 들어가야 할 상자는 4번, 두번째로 들어가야 할 상자는 3번, 3번째로 들어가야 할 상자는 1번 ...
# deque와 stack으로..

import collections

def solution(order):
    answer = 0
    belt = collections.deque([i for i in range(1, len(order) + 1)])
    sub_belt = []

    idx = 0
    while belt or sub_belt:
        if belt and belt[0] == order[idx]:
            belt.popleft()
            answer += 1
            idx += 1
        elif sub_belt and sub_belt[-1] == order[idx]:
            sub_belt.pop()
            answer += 1
            idx += 1
        else:
            if belt:
                sub_belt.append(belt.popleft())
            else:
                break

    return answer
