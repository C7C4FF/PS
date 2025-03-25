# https://leetcode.com/problems/check-if-grid-can-be-cut-into-sections/description/?envType=daily-question&envId=2025-03-25

# y = i, j , x = i, j 의 선을 구할 때 각각 정렬 한번씩 해주기 (효율성은 떨어질 것 같은데)
# n은 왜 있는 걸까...?


class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        # horizontal 검사 -> y 좌표 이용
        rectangles.sort(key=lambda r: r[1])
        
        horizontal = 1
        h_y = rectangles[0][3]

        for start_x, start_y, end_x, end_y in rectangles[1:]:
            # 두 직사각형이 분리 되어 있음. -> 그룹이 하나 늘어남
            if start_y >= h_y:
                horizontal += 1
            
            h_y = max(h_y, end_y)
        
        # vertical 검사 -> x 좌표 이용
        rectangles.sort()
        vertical = 1
        v_x = rectangles[0][2]

        for start_x, start_y, end_x, end_y in rectangles[1:]:
            if start_x >= v_x:
                vertical += 1
                
            v_x = max(v_x, end_x)
        
        # 3 그룹 이상이기만 하면 2개의 선으로 나눌 수 있음
        # 4 그룹이 나오면 ( A+B / C / D ) ( A / B + C / D) .. 등
        return horizontal >= 3 or vertical >= 3
