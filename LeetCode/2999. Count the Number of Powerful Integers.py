# https://leetcode.com/problems/count-the-number-of-powerful-integers/?envType=daily-question&envId=2025-04-10
# editorial #2 
# Digit DP도 공부하기

class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        # 구간 [start, finish] 을 [0, finish]와 [0, start-1] 의 차이로 계산
        start_ = str(start - 1)
        finish_ = str(finish)
        return self.calculate(finish_, s, limit) - self.calculate(start_, s, limit)

    def calculate(self, x: str, s: str, limit: int) -> int:
        """
        문자열 x까지 만들 수 있는, '각 자리수가 0~limit' 인 숫자들 중
        끝이 s로 끝나는 접두사의 개수를 누적 계산
        """

        # x가 접미사 s보다 자릿수가 작으면 해당하는 숫자가 없음.
        if len(x) < len(s):
            return 0
        # x와 s의 길이가 같으면, x 자체가 s 이상이면 1, 아니면 0
        if len(x) == len(s):
            return 1 if x >= s else 0

        count = 0
        suffix = x[-len(s):] # s 접미를 붙을 부분을 위해 제거
        pre_len = len(x) - len(s) # 접두 부분의 길이

        # 접두사 각 자리마다 가능한 경우의 수를 누적 계산
        for i in range(pre_len):
            # 현재 자리의 숫자가 limit보다 크면,
            # 남은 자리수에 대해 (limit+1)**(남은 자리수) 전부 허용되므로 바로 더해주고 종료
            if int(x[i]) > limit:
                count += (limit + 1) ** (pre_len - i)
                return count
            # 현재 자리보다 작은 숫자들에 대해, 남은 자리수 조합 수를 곱해서 누적
            count += int(x[i]) * (limit + 1) ** (pre_len - 1 - i)
        
        # x의 접미사(끝 부분)가 s 이상이면 하나의 경우가 추가
        if suffix >= s:
            count += 1
        
        return count

'''
# TLE 245/932

class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        # s 중에 limit을 넘는 게 있으면 존재할 수 없음
        # for digit in s:
        #     if int(digit) > limit:
        #         return 0

        suffix_n = len(s)
        n = len(str(finish))

        # 가능한 자리수
        max_length = n - suffix_n
        
        ans = set()

        for i in range(max_length+1):
            for j in product([str(x) for x in range(limit+1)], repeat=i):
                prefix = "".join(j)
                target = int(prefix+s)

                if target > finish or target < start:
                    pass
                else:
                    ans.add(target)

        return len(ans)
'''
