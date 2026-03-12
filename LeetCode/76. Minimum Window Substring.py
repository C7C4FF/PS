# https://leetcode.com/problems/minimum-window-substring/description/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        unique = set(t)
        target_cnt = Counter(t)

        window = {}
        unique_target = 0

        l, r = 0, 0
        ans = [0, len(s) + 1]

        while r < len(s):
            ch = s[r]
            window[ch] = window.get(ch, 0) + 1

            # 요구사항만큼 갯수가 있으면 + 1
            if window[ch] == target_cnt[ch]:
                unique_target += 1

            # 문자별 요구사항을 모두 만족했다면
            while l <= r and len(unique) == unique_target:
                # 최단 길이일 때만 갱신
                if ans[1] - ans[0] > r - l:
                    ans = [l, r]

                ch = s[l]
                window[ch] -= 1

                # 요구사항보다 갯수가 부족해졌다면 - 1
                if window[ch] < target_cnt[ch]:
                    unique_target -= 1

                l += 1

            r += 1

        if ans[1] > len(s):
            return ""
        else:
            return s[ans[0]:ans[1]+1]

'''
# TLE
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        string_len = len(s)
        target_len = len(t)

        target_cnt = Counter(t)
        window_len = target_len

        while window_len <= string_len:
            for i in range(string_len - window_len + 1):
                target = s[i:i+window_len]
                seen = Counter(target)
                if all(seen[ch] >= cnt for ch, cnt in target_cnt.items()):
                    return target
            
            window_len += 1
        
        return ""
'''
