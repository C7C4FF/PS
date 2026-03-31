# https://leetcode.com/problems/bitwise-and-of-numbers-range/description/
# 브라이언 커니핸 .. 
# 큰 수부터 시작해서 맨 오른쪽의 bit를 없애가면서 확인 > 최대 32번만 하면 됨
# left 보다 작거나 같아질 때 > 두 숫자의 공통 비트만 남고 다 없어짐

class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        while right > left:
            right = right & (right-1)
        
        return right
