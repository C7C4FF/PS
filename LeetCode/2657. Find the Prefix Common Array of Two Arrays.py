# https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/?envType=daily-question&envId=2026-05-20
# 1보다 큰 게 아니라, 2일 때만 세면 됨
# 더하고, 두번 나왔는 지 확인하기

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        freq = [0] * (n+1)
        
        ans = []
        cnt = 0

        for a, b in zip(A, B):
            freq[a] += 1
            if freq[a] == 2:
                cnt += 1

            freq[b] += 1
            if freq[b] == 2:
                cnt += 1

            ans.append(cnt)
        
        return ans
        


'''
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        n = len(A)
        total = defaultdict(int)

        ans = []
        cnt = 0
        for i in range(n):
            num1, num2 = A[i], B[i]
            total[num1] += 1
            total[num2] += 1

            if num1 == num2:

                if total[num1] > 1:
                    cnt += 1

            else:
                if total[num1] > 1:
                    cnt += 1
                if total[num2] > 1:
                    cnt += 1
            
            ans.append(cnt)

        return ans
'''
