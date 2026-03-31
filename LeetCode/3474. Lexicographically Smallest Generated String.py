# https://leetcode.com/problems/lexicographically-smallest-generated-string/description/?envType=daily-question&envId=2026-03-31

# 먼저 확정된 문자들을 전부 넣고, 그 외의 빈 칸은 '.' 으로 채워넣기
# 사전순으로 가장 작은 글자를 구하는 것이기 때문에 넣을 수 있는 글자는 'a', 'b' 두가지 경우만 사용하면 됨

class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        words = []

        for i in range(n):
            if str1[i] == "T":
                words.append((i, str2))
            else:
                words.append((i, "."*m))

        last_idx, last_ch = words[-1]
        word_length = last_idx + m
        result = ['.'] * word_length
        
        for idx, ch in words:
            for i, char in enumerate(ch):
                if char != '.':
                    if result[idx + i] != "." and result[idx + i] != char: # 반례 1) [(0, 'abc'), (2, 'abc')] 처럼 중복되는데 글자가 다른 경우 
                        return ""
                    else:
                        result[idx + i] = char
        
        blank = set()
        for i in range(word_length):
            if result[i] == '.':
                blank.add(i)
                result[i] = 'a' # 일단 전부 'a'로 채우기

        for i in range(n):
            if str1[i] == "F":
                if "".join(result[i:i+m]) == str2: # F라서 str2 와 같지 않아야 하는데, 같게 됐을 때
                    target = -1
                    for j in range(i+m-1, i-1, -1):
                        if j in blank:
                            target = j # 빈칸이었던 ('.' 이었던) 가장 뒷자리 찾기
                            break
                    
                    if target == -1: # 그 안에 빈칸이 없었다면 성립할 수 없음으로 반환
                        return ""

                    current = result[target]
                    conflict = str2[target-i]
                    
                    avoid_conflict = ord(conflict) + 1 # 딱 하나 올려주기
                    
                    if chr(avoid_conflict) == conflict:
                        avoid_conflict += 1 # 같았다면 하나 더 올려주기

                    result[target] = chr(avoid_conflict)


        return "".join(result)
