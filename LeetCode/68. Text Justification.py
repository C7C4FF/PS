# https://leetcode.com/problems/text-justification/description/


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ans = []

        sep = []
        length = 0
        line = []

        for word in words:
            length += len(word)

            if length <= maxWidth:
                line.append(word)
                length += 1 # 사이에 공백을 계산하기 위한 + 1
            else:
                sep.append(line)
                line = [word]
                length = len(word) + 1
        
        sep.append(line) # 못 들어간 나머지 단어 넣어주기
        
        for i in range(len(sep)): # 문장 완성하기
            lst = sep[i]
            cnt = len(lst)
            temp = " ".join(lst)

            short = maxWidth - len(temp)
            
            if i == len(sep) - 1: # 마지막 문장이라면, 왼쪽 정렬이기에 모든 문자를 이어붙이고, 모자란 양만큼 공백 채우기
                temp += " " * short
                ans.append(temp)
            else:
                if cnt == 1: # 단어 1개만 있다면, 부족한 수만큼 뒤에 공백 붙이기
                    temp += " " * short
                    ans.append(temp)
                elif cnt == 2: # 단어 2개라면, 사이에 공백 넣기
                    spaces = " " + " " * short
                    ans.append(f"{lst[0]}{spaces}{lst[1]}")
                else: # 3개 이상은 앞에서부터 채우기.
                    q, r = divmod(short, (cnt - 1)) # q : 모든 곳에 q개씩 들어감, r: 앞에서부터 1개씩 들어감
                    if q > 0:
                        spaces = [" " + " " * q for _ in range(cnt - 1)]
                    else:
                        spaces = [" " for _ in range(cnt - 1)]

                    for i in range(r):
                        spaces[i] += " "
                    
                    sentence = ""
                    for i in range(len(spaces)):
                        sentence += lst[i] + spaces[i]
                    sentence += lst[-1]

                    ans.append(sentence)
        
        return ans
