# https://leetcode.com/problems/apply-operations-to-maximize-score/description/?envType=daily-question&envId=2025-03-29

# 1점에서 시작해서 k번까지 연산을 반복해서 점수를 최대화하기
# 비어있지 않고, 이전까지 선택하지 않았던 nums[l:r+1] subarray 고르기.
# nums[l:r+1] 안의 nums[i] 들은 소인수분해를 해서 소인수가 몇개인지가 prime score가 됨.
#  ㄴ 안에서 prime score가 가장 낮은 수를 골라 곱하기

# 매번 소인수 분해를 하기에는 시간 초과가 나지 않을까.. -> 괜찮았다..
# 에라토스테네스의 체를 사용하는 게 효율적

# 짜다 막혀서 editorial 보고 작성..

class Solution:
    def prime_factorization(self, num: int) -> int:
        ''' 소인수 분해를 하고, 그 소수의 개수를 반환하는 함수'''
        cnt = set()
        x = 2
        
        while x <= int(math.sqrt(num)):
            if num % x == 0:
                if x not in cnt:
                    cnt.add(x)
                num //= x
            else:
                x += 1
        
        # 2보다 크거나 같으면 소수가 하나 더 있음
        if num >= 2:
            cnt.add(num)

        return len(cnt)
                
    def maximumScore(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix = defaultdict(int)

        # prime score 계산
        for i in range(len(nums)):
            prefix[i] = self.prime_factorization(nums[i])


        next_dominant = [n] * n
        prev_dominant = [-1] * n
        
        # Stack to store indices for monotonic decreasing prime score
        monotonic_stack = []

        # 각 숫자에 이전, 이후 큰 숫자를 계산하기
        for index in range(n):
            # 현재 num이 stack의 top보다 크다면, stack의 모든 원소에 대해 다음 큰 원소를 기록
            while (monotonic_stack and prefix[monotonic_stack[-1]] < prefix[index]):
                top_index = monotonic_stack.pop()
                
                # top_index 위치의 원소는 i 위치의 원소를 '다음 큰 수'로 갖는다
                next_dominant[top_index] = index
            
            # 스택이 비어있지 않다면, 스택 top의 인덱스는 현재 값보다 왼쪽에 있는 더 큰 값
            if monotonic_stack:
                prev_dominant[index] = monotonic_stack[-1]
            
            monotonic_stack.append(index)

        # subarrays 중 최대 (dominant한) 원소 찾기
        num_of_subarrays = [0] * n
        for index in range(n):
            num_of_subarrays[index] = (next_dominant[index] - index) * (
                index - prev_dominant[index]
            )

        # Priority queue to process elements in decreasing order of their value
        priority_queue = []

        for index in range(n):
            heapq.heappush(priority_queue, (-nums[index], index))
        
        score = 1

        # 분할 정복으로 모듈러 연산하기
        # O(exponent) -> O(log exponent) 시간에 연산 가능
        def _power(base, exponent):
            res = 1

            while exponent > 0:
                if exponent % 2 == 1:
                    res = (res * base) % (10**9 + 7)

                base = (base * base) % (10**9 + 7)
                exponent //= 2
            
            return res
        
        while k > 0:
            # 현재 priority_queue에서 가장 큰 값을 pop (음수로 저장했으므로 다시 양수로 복원)
            num, index = heapq.heappop(priority_queue)
            num = -num

            # 현재 원소가 우세한 구간의 개수만큼 곱할 수 있음, 단 남은 k를 초과하지 않도록 제한
            operations = min(k, num_of_subarrays[index])
            
            # operations 수만큼 거듭제곱 후 모듈러 연산 진행
            score = (score * _power(num, operations)) % (10**9 + 7)

            # 사용한 연산 수만큼 k 감소
            k -= operations
        
        return score
