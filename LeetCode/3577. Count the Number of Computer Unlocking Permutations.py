# complexity[0] : decrypted, 순열의 맨 처음. 이 수보다 큰 수들은 이걸로 전부 풀 수 있음.
# complexity[0]이 유일한 값이 아니거나, 그보다 작은 값이 있다면 모든 컴퓨터를 풀 수 없음
# 그 외에는 전부 0으로 풀 수 있기 때문에 순서에 상관없이 가능한 모든 순열을 구하면 됨

class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        n = len(complexity)
        first = complexity[0]
        
        cnt = Counter(complexity)

        if cnt[first] != 1 or any(k < first for k in cnt):
            return 0
        else:
            return math.factorial(n-1) % (10**9 + 7)
