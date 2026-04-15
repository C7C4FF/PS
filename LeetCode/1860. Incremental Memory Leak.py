# https://leetcode.com/problems/incremental-memory-leak/description/
# 1씩 증가해서 2^32 를 전부 없애려면 92,682초가 필요

class Solution:
    def memLeak(self, memory1: int, memory2: int) -> List[int]:
        cnt = 1
        
        while cnt < 1000000:
            if max(memory1, memory2) < cnt:
                return [cnt, memory1, memory2]

            if memory1 >= memory2:
                memory1 -= cnt
            else:
                memory2 -= cnt
                
            cnt += 1
