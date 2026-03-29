# https://leetcode.com/problems/check-if-strings-can-be-made-equal-with-operations-ii/description/
# 글자가 모두 똑같이 있는지 확인하기 위해 set 사용
# 홀수는 홀수자리에, 짝수는 짝수 자리에 존재해야 함

class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        ch = defaultdict(list)
        ch2 = defaultdict(list)

        set_s1 = set(s1)
        set_s2 = set(s2)

        if set_s1 != set_s2:
            return False

        for i in range(len(s1)):
            ch[s1[i]] += [i]
            ch2[s2[i]] += [i]

        for k in ch:
            odd, even = 0, 0
            odd2, even2 = 0, 0

            for i in ch[k]:
                if i % 2 == 0:
                    even += 1
                else:
                    odd += 1
            for i in ch2[k]:
                if i % 2 == 0:
                    even2 += 1
                else:
                    odd2 += 1

            if (even != even2) or (odd != odd2):
                return False
        
        return True
