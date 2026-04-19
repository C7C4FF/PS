# https://leetcode.com/problems/previous-permutation-with-one-swap/description/

class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        n = len(arr)
        idx = -1
        
        # 역순으로 돌면서 처음으로 감소하는 구간 찾기 
        for i in range(n-2, -1, -1):
            if arr[i+1] < arr[i]:
                idx = i
                break
        
        # 없으면 원래 배열 반환 
        if idx == -1:
            return arr

        # idx 이후 숫자들 중 arr[idx] 보다 작으면서 가장 큰 값 찾기
        max_idx = -1
        for i in range(n-1, idx, -1):
            if arr[i] < arr[idx]:
                if max_idx == -1 or arr[i] >= arr[max_idx]:
                    max_idx = i
        
        # 스왑하기
        arr[idx], arr[max_idx] = arr[max_idx], arr[idx]

        return arr
            
        
