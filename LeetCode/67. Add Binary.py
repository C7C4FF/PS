# https://leetcode.com/problems/add-binary/?envType=daily-question&envId=2026-02-15
# return bin(int(a, 2) + int(b, 2))[2:] 로 간단하게 할 수 있어

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        lst_a = list(a)
        lst_b = list(b)
        length = max(len(lst_a), len(lst_b))
        ans = [0 * i for i in range(length+1)]
        
        for i in range(max(len(lst_a), len(lst_b))):
            if lst_a and lst_b:
                bit_a, bit_b = lst_a.pop(), lst_b.pop()
            elif lst_a and not lst_b:
                bit_a, bit_b = lst_a.pop(), 0
            else:
                bit_a, bit_b = 0, lst_b.pop()

            target = int(bit_a) + int(bit_b) + int(ans[i])
            ans[i] = str(target % 2)
            ans[i+1] = str(target // 2)

        if ans[-1] == "0":
            ans.pop()
            
        ans = ''.join(ans[::-1])
        
        return ans
