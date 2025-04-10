# https://leetcode.com/problems/powerful-integers/
# 엣지케이스 bound가 2보다 작을 경우, x 혹은 y가 1인 경우

class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        # 2보다는 작을 수 없음
        if bound < 2:
            return []

        ans = set()

        if x == 1 and y == 1:
            return [2]
        
        i = 0
        x_lst = [1]
        if x != 1:
            while x**i <= bound:
                target = x**i
                if target <= bound:
                    x_lst.append(target)
                i += 1
        
        j = 0
        y_lst = [1]
        if y != 1:
            while y**j <= bound:
                target = y**j
                if target <= bound:
                    y_lst.append(target)
                j += 1
        
        for x_result in x_lst:
            for y_result in y_lst:
                target = x_result + y_result
                if target <= bound:
                    ans.add(target)
        
        return list(ans)
