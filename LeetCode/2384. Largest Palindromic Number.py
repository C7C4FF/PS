# https://leetcode.com/problems/largest-palindromic-number/description/

class Solution:
    def largestPalindromic(self, num: str) -> str:
        cnt = Counter(num)
        odd, even = [], []

        for k, v in cnt.items():
            q, r = divmod(v, 2)
            if q:
                heapq.heappush(even, (-int(k), q))
            if r:
                heapq.heappush(odd, (-int(k), r))

        ans = ''
        for _ in range(len(even)):
            k,v = heapq.heappop(even)
            if ans == '' and k == 0: # leading zero 없애기
                break
            ans += str(-k) * v
        
        mid = ""
        if odd:
            k, v = heapq.heappop(odd)
            mid = str(-k)
        
        if not ans and not mid:
            return "0"
        else:
            return ans + mid + ans[::-1]
