# https://leetcode.com/problems/uncommon-words-from-two-sentences/description/
# 상대 문장에 등장하지 않은 것이 uncommon 한 게 아니라
# 문장에 딱 1번만 등장하고, 상대 문장에 등장하지 않은 것이 uncommon

class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        word_s1 = s1.split(" ")
        word_s2 = s2.split(" ")
        cnt_s1 = Counter(word_s1)
        cnt_s2 = Counter(word_s2)

        potential_uncommon = list(set(word_s1) ^ set(word_s2))
        ans = []

        for word in potential_uncommon:
            if cnt_s1[word] == 1 or cnt_s2[word] == 1:
                ans.append(word)
        
        return ans
