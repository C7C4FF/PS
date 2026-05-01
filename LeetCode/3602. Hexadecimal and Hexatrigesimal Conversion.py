# https://leetcode.com/problems/hexadecimal-and-hexatrigesimal-conversion/description/
# string.digits .. 등으로 리스트 컴프리헨션 대신 쓸 수도 있음
# 가장 작은 자릿수부터 시작하기 때문에 뒤집어주기

class Solution:
    def concatHex36(self, n: int) -> str:
        square, cube = n**2, n**3
        
        # 0-9A-Z
        digits = string.digits + string.ascii_uppercase

        s = ''
        while square:
            s += digits[square % 16]
            square //= 16
        
        c = ''
        while cube:
            c += digits[cube % 36]
            cube //= 36

        return s[::-1] + c[::-1]
            




