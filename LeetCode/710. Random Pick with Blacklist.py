# https://leetcode.com/problems/random-pick-with-blacklist/
# 블랙 리스트를 매번 조회하는 건 TLE .. 
# 리스트로 조회하는 것보다 집합으로 만들어서 조회하는 게 더 빠름
# 블랙리스트 대신에 화이트리스트를 만들기 > 블랙리스트에 들어있는 숫자를 화이트리스트의 다른 숫자로 매핑하기

class Solution:
    def __init__(self, n: int, blacklist: List[int]):
        self.scope = n - len(blacklist)
        self.whitelist = {}

        any_number = n - 1
        blacklist_set = set(blacklist)

        for banned in blacklist:
            if banned < self.scope:
                while any_number in blacklist_set:
                    any_number -= 1
                self.whitelist[banned] = any_number
                any_number -= 1

    def pick(self) -> int:
        target = random.randint(0, self.scope - 1)
        return self.whitelist.get(target, target)


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()
