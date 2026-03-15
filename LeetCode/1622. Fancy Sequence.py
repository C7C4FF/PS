# https://leetcode.com/problems/fancy-sequence/?envType=daily-question&envId=2026-03-15
# 계산을 매번 업데이트하는 게 아니라, 현재까지 들어온 inc, m 으로 역산하고 넣어줘서, 꺼낼 때 한번에 계산
# inversion_val = (val - self.added) / self.mul 로 구하면 float는 정밀도를 잃어버림
# pow(self.mul, -1, self.MOD) => self.mul 로 나눈 값이랑 똑같은 정수를 찾아줌

class Fancy:

    def __init__(self):
        self.MOD = 10**9 + 7
        self.lst = []
        self.added = 0
        self.mul = 1
        self.n = 0

    def append(self, val: int) -> None:
        inversion_val = (val - self.added) * pow(self.mul, -1, self.MOD)
        self.lst += [inversion_val]
        self.n += 1

    def addAll(self, inc: int) -> None:
        self.added = (self.added + inc) % self.MOD

    def multAll(self, m: int) -> None:
        self.mul = (self.mul * m) % self.MOD
        self.added = (self.added * m) % self.MOD

    def getIndex(self, idx: int) -> int:
        if idx < 0 or idx >= self.n:
            return -1
        else:
            return int((self.lst[idx] * self.mul + self.added)) % self.MOD

# Your Fancy object will be instantiated and called as such:
# obj = Fancy()
# obj.append(val)
# obj.addAll(inc)
# obj.multAll(m)
# param_4 = obj.getIndex(idx)
