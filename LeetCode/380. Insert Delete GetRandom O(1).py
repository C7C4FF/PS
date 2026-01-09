# https://leetcode.com/problems/insert-delete-getrandom-o1/?envType=study-plan-v2&envId=top-interview-150
# set() 하나만 하는 경우에서는 random.choice(list()) 과정에서 list(set()) 이 O(n) 이 됨
# 리스트와 해시맵을 사용하기...

class RandomizedSet:

    def __init__(self):
        self.dict = {}
        self.lst = []

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False
        else:
            self.dict[val] = len(self.lst)
            self.lst.append(val)
            return True

    def remove(self, val: int) -> bool:
        if val not in self.dict:
            return False
        else:
            index = self.dict[val]
            last = self.lst[-1]
            
            # 마지막 원소를, 지울 원소 자리에 넣기
            # [1, 2, 3, 4] 중 2를 지운다고 하면 [1, 4, 3, 4] -> [1, 4, 3] 
            self.lst[index] = last
            self.dict[last] = index

            self.lst.pop()
            del self.dict[val]
            
            return True

    def getRandom(self) -> int:
        return random.choice(self.lst)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
