# https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-ii/description/
# https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-ii/editorial/
# https://leetcode.com/problems/maximum-difference-between-even-and-odd-frequency-ii/solutions/6831146/easy-to-understand-explanation-for-edito-0bca/

# 0, 1, 2, 3, 4 중 2개를 골라서 조건을 만족하도록 만들기 > 모든 경우의 수를 체크하기 (총 20가지 경우)
# s[i:j] 에 대해서 prefix sums 으로 구하기. 0~j 까지의 수 - 0~i-1 까지의 수
# freq[a] - freq[b] 가 최대가 되어야 함. (s[:j].count(a) - s[:j].count(b)) - (s[:i].count(a) - s[:i].count(b))

# 홀-짝:홀, 짝-홀: 홀, 홀-홀: 짝, 짝-짝: 짝 , freq[a] 는 홀수여야 하고, freq[b]는 짝수여야 함.
# 홀수인 경우를 1. 짝수인 경우를 0으로 생각한다면 .. 우리의 목표는 parity가 10이어야 함
# ((cnt_a & 1) << 1) | (cnt_b & 1) -> cnt_a 가 홀짝인지 판별 후 자릿수 올림. cnt_b가 홀짝인지 판별
# cnt_a가 홀수, cnt_b가 짝수인 경우를 찾기

class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        n = len(s)
        ans = float('-inf')

        def get_status(cnt_a: int, cnt_b: int) -> int:
            # cnt_a, cnt_b 의 홀짝 판별
            # bit 1: parity of cnt_a. bit 0: parity of cnt_b
            return ((cnt_a & 1) << 1) | (cnt_b & 1)

        for a in ["0", "1", "2", "3", "4"]:
            for b in ["0", "1", "2", "3", "4"]:
                if a == b:
                    continue
                
                best = [float('inf')] * 4   # parity (0~3) 별로 (prev_a - prev_b) 가 가장 작은 경우를 담아둠.
                cnt_a, cnt_b = 0, 0         # right 포인터 s[0...right] 안에 얼마나 들어있는지
                prev_a, prev_b = 0, 0       # left 포인터 s[0...left] 안에 얼마나 들어있는지
                left = -1                   # end of prefix

                for right, char in enumerate(s):
                    if char == a: cnt_a += 1    # char = s[right]
                    if char == b: cnt_b += 1    # a, b 가 현재 쌍의 숫자와 같을 때마다 +1

                    # substring (left+1 ~ right) 이 조건을 만족하도록 순회하기
                    # 최소 길이는 k여야 하고, 문자 b가 0이 아닌 짝수가 될 수 있는 경우에만 확인
                    while right - left >= k and cnt_b - prev_b >= 2:
                        left_status = get_status(prev_a, prev_b)    # left에서 끝나는 subs 의 parity 체크
                        
                        # (prev_a - prev_b) 의 최솟값을 저장하기
                        best[left_status] = min(best[left_status], prev_a - prev_b) 

                        # 앞쪽으로 왼쪽 포인터를 하나씩 옮기기
                        left += 1
                        if s[left] == a: prev_a += 1
                        if s[left] == b: prev_b += 1

                    right_status = get_status(cnt_a, cnt_b)     # right 까지의 parity 체크

                    # 우리의 목표는 parity 가 10이어야 함. 0b10 = left_status ^ right_status
                    # 즉 우리가 찾아야 할 left_status = right_status XOR 10
                    required_status = right_status ^ 0b10
                    if best[required_status] != float('inf'):
                        # (cnt_a - cnt_b) - min(prev_a - prev_b) 구하기
                        ans = max(ans, cnt_a - cnt_b - best[required_status])

        return ans


                    
