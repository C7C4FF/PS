# https://leetcode.com/problems/product-of-the-last-k-numbers/?envType=daily-question&envId=2025-02-14
# 0 이 나오면 리스트 초기화하기
# 이제까지 모든 수를 곱해 리스트에 넣기. 그리고 나눗셈으로 k번째까지의 연산 수행

class ProductOfNumbers:
    def __init__(self):
        self.lst = [1]
        self.n = 1

    def add(self, num: int) -> None:
        if num == 0:
            self.lst = [1]
            self.n = 1
        else:
            self.lst.append(self.lst[-1]*num)
            self.n += 1


    def getProduct(self, k: int) -> int:
        if self.n <= k:
            return 0
        else:
            return int(self.lst[-1]/self.lst[-1-k])


# ["ProductOfNumbers","add","add","add","add","add","getProduct","getProduct","getProduct","add","getProduct"]
# [         [],         [3], [0],   [2], [5],   [4],    [2],        [3],          [4],      [8],    [2]]
# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
