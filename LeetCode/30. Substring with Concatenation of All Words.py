# https://leetcode.com/problems/substring-with-concatenation-of-all-words/description/
# permutations 으로 모든 조합을 만들기 > MLE

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        ans = []

        window_len = len(words) * len(words[0])
        word_len = len(words[0])
        word_freq = Counter(words)
        
        for i in range(len(s) - window_len + 1):
            seen = {}
            j = i

            while j < i + window_len:
                current_word = s[j:j+word_len]

                if current_word in word_freq:
                    seen[current_word] = 1 + seen.get(current_word, 0)
                    if seen[current_word] > word_freq[current_word]:
                    # 해당 단어가 words 보다 더 많이 등장했다면 > 불가능
                        break
                else:
                # words 에 없는 단어라면 > 불가능
                    break

                j += word_len  # 옆으로 옮기기
            
            if j == i + window_len:
                ans.append(i)
                
        return ans
