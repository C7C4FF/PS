# https://leetcode.com/problems/decode-the-slanted-ciphertext/description/?envType=daily-question&envId=2026-04-04

# 총 길이 / rows 만큼해서 문자를 원래대로 만들어주기
# (0,0) 부터 오른쪽 대각선으로 하나씩 하면서 문자 넣기
# 공백은 rstrip으로 오른쪽 공백만 지우기

class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        if rows == 1:
            return encodedText

        ans = ""
        n = len(encodedText)
        row = n // rows

        lst = [encodedText[i*row:i*row+row] for i in range(rows)]

        for i in range(row):
            for j in range(rows):
                if j >= n or j >= rows or i+j >= n or i+j >= row:
                    break
                else:
                    ans += lst[j][i+j]

        return ans.rstrip()
