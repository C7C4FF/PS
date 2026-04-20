# https://leetcode.com/problems/minimum-deletions-to-make-string-k-special/description/
# og_v 를 최소로 등장할 수 있는 수라고 가정하고 계산 진행
# og_v 보다 작다면 그걸 아예 지워버림, og_v + k 보다 크다면 빼줌

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        ans = float('inf')
        cnt = Counter(word)

        for og_k, og_v in cnt.items():
            remove = 0
            for next_k, v in cnt.items():
                if og_k == next_k: continue

                if og_v > v:
                    remove += v
                elif v > (og_v + k):
                    remove += (v - og_v - k)
                else:
                    continue

            ans = min(ans, remove)

        return ans
        
