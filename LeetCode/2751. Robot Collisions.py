# https://leetcode.com/problems/robot-collisions/description/?envType=daily-question&envId=2026-04-01


class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        remain = [] # 왼쪽으로 지나간 로봇 (충돌하지 않는 로봇)

        robots = [] # 힙으로 실제 위치 (postions) 순서대로 정렬
        for i in range(n):
            heapq.heappush(robots, (positions[i], healths[i], directions[i], i)) # position, health, directions, 원래 index
        
        r = []
        for i in range(n):
            p, h, d, original_pos = heapq.heappop(robots)
    
            if d == 'R':
                r.append([h, original_pos])
            else:
                while r and h > 0:
                    collide_robot, collide_pos = r[-1]

                    if h > collide_robot: # L이 더 큼 > 계속 전투함
                        r.pop()
                        h -= 1
                    elif h == collide_robot: # L == R > 둘다 사라짐
                        r.pop()
                        h = 0
                    else: # R이 더 큼 > R 로봇 피 -1 후 종료
                        r[-1][0] -= 1
                        h = 0

                if h > 0:
                    remain.append([h, original_pos])

        remain += r
        remain.sort(key=lambda x:x[1]) # 원래 idx 순으로 정렬
        
        ans = [h for h, p in remain]

        return ans
        

    
