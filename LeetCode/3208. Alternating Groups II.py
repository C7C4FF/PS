# https://leetcode.com/problems/alternating-groups-ii/?envType=daily-question&envId=2025-03-09

# 윈도우 크기를 k로 두고, 동일한지 확인하기
# 1010101 .. 서로 다 다른 group이 하나 있고, 거기서부터 시작하고 싶긴 함
# -> 누적합으로?

# 슬라이딩 윈도우 풀이... size 로 계속 비교하고 있었는데, 굳이 변수를 하나 더 쓸 필요는 없어보임

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        ans = 0
        circular = colors + colors[:k-1]

        left = 0
        right = 1

        while right < len(circular):
            # 둘이 서로 다르다면 오른쪽으로 한칸씩, 
            if circular[right-1] != circular[right]:
                right += 1
            else:
            # 둘이 같다면 그 이전까지 다시 살펴볼 필요 X. 바로 left 포인터를 right로 바꿔줌
                left = right
                right = left + 1

            if right - left < k:
                continue
            
            ans += 1
            left += 1

        return ans
