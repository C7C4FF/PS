# https://leetcode.com/problems/walking-robot-simulation-ii/description/?envType=daily-question&envId=2026-04-07
# num이 너무 큼 > 둘레로 나누기. 몫은 바퀴 수니 무시하고, 남은 나머지는 움직이기
# 0,0 에서 계속 둘레의 배수만큼 움직여서 결국 0,0 으로 왔다면 진행 방향을 south로 바꿔줘야 함

class Robot:

    def __init__(self, width: int, height: int):
        self.directions = ['East', 'North', 'West', 'South',]
        self.heading = 0

        self.width = width - 1
        self.height = height - 1

        self.pos = [0, 0]

    def step(self, num: int) -> None:
        num %= self.width*2 + self.height*2

        if num == 0:
            if self.pos == [0, 0]:
                self.heading = 3
        
        while num > 0:
            if self.directions[self.heading] == "East":
                move = min(num, self.width - self.pos[0])
                self.pos[0] += move
                num -= move
                if num > 0:
                    self.heading = 1

            elif self.directions[self.heading] == "North":
                move = min(num, self.height - self.pos[1])
                self.pos[1] += move
                num -= move
                if num > 0:
                    self.heading = 2

            elif self.directions[self.heading] == "West":
                move = min(num, self.pos[0])
                self.pos[0] -= move
                num -= move
                if num > 0:
                    self.heading = 3
            else:
                move = min(num, self.pos[1])
                self.pos[1] -= move
                num -= move
                if num > 0:
                    self.heading = 0

    def getPos(self) -> List[int]:
        return self.pos

    def getDir(self) -> str:
        return self.directions[self.heading]
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()
