# https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/
# https://leetcode.com/problems/remove-duplicate-letters/ 와 동일한 문제

class Solution:
    def smallestSubsequence(self, s: str) -> str:
        counter, seen, stack = Counter(s), set(), []

        for char in s:
            counter[char] -= 1
            if char in seen:
                continue
            # 뒤에 붙일 문자가 남아 있다면 스택에서 제거
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            stack.append(char)
            seen.add(char)

        return ''.join(stack)
