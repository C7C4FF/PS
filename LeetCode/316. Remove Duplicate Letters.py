# https://leetcode.com/problems/remove-duplicate-letters/
# 사전순 정렬 -> 결국 결과로 나오는 값은 알파벳당 한번씩만 나와야 함
# 하나밖에 없으면 위치는 고정

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        cnt = Counter(s)
        stack = []

        for ch in s:
            cnt[ch] -= 1
            if ch in stack:
                continue
            # 뒤에 붙일 문자가 남아 있다면 스택에서 제거
            while stack and ch < stack[-1] and cnt[stack[-1]] > 0:
                stack.pop()
            stack.append(ch)

        return ''.join(stack)

'''
# 스택에서 사용 가능한 연산만을 수행, 검색은 seen 변수를 만들어서 수행
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
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

'''
