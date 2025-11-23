# https://leetcode.com/problems/vowel-spellchecker/description/

class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        def vowel_to_asterisk(word: str) -> str:
            vowels = set("aeiou")
            return ''.join('*' if c in vowels else c for c in word.lower())

        exact = set(wordlist)
        lower_map = {}
        vowel_insen_map = {}

        for w in wordlist:
            wl = w.lower()
            lower_map.setdefault(wl, w)
            vowel_insen_map.setdefault(vowel_to_asterisk(w), w)

        answer = []
        for q in queries:
            if q in exact:
                answer.append(q)
                continue

            ql = q.lower()
            if ql in lower_map:
                answer.append(lower_map[ql])
                continue

            dq = vowel_to_asterisk(q)
            answer.append(vowel_insen_map.get(dq, ""))

        return answer
