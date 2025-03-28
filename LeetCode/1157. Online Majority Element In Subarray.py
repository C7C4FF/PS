# https://leetcode.com/problems/online-majority-element-in-subarray/

# Buyer-Moore Voting 단순 구현으로는 TLE 가 남,,
# 2780. Minimum Index of a Valid Split 랑 다르게 각 subarray 마다 majority element가 다름
#   -> prefix 배열을 미리 맘대로 만들어두는건 쫌 힘들지도
#   => hashmap으로 해당 element가 어느 index에 존재하는지 리스트로 만들어두기...

# 힌트는 majority element는 나올 확률 p가 50프로 이상이니까,
# 특정 원소를 뽑을 때 그게 m.e 가 아닐 확률은 (1 - p)...
# 50프로로 잡아도 모두 안 나올 확률은 (1/2)^10 = 1/1024 ≒ 0.1%, ^20 ≒ 0.00001%, ^30 ≒ 0.0000000001%
# 이걸 많이 반복하면 정답이 아닐 확률이 0에 가까워진다...


class MajorityChecker:
    def __init__(self, arr: List[int]):
        self.arr = arr
        self.pos = defaultdict(list)

        # 해당 element가 어느 index에 존재하는지 저장
        for i, v in enumerate(arr):
            self.pos[v].append(i)

    def query(self, left: int, right: int, threshold: int) -> int:
        for _ in range(30):
            idx = random.randint(left, right)
            candidate = self.arr[idx]
            pos_list = self.pos[candidate]

            l = bisect.bisect_left(pos_list, left)
            r = bisect.bisect_right(pos_list, right)
            cnt = r - l

            # 이진 탐색으로 [left, right] 구간 내 candidate의 등장 횟수 계산
            if cnt >= threshold:
                return candidate

        return -1
        
        

        

'''
# 29/37 TLE
    def query(self, left: int, right: int, threshold: int) -> int:
    
        cnt = 0
        major = 0
        
        array = self.arr[left:right+1]
        n = len(array)
        
        for num in array:
            if cnt == 0:
                major = num
            cnt += 1 if major == num else -1

        if cnt > 0 and array.count(major) >= threshold:
            return major
        else:
            return -1
'''


# Your MajorityChecker object will be instantiated and called as such:
# obj = MajorityChecker(arr)
# param_1 = obj.query(left,right,threshold)
