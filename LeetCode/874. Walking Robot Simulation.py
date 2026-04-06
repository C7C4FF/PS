# https://leetcode.com/problems/walking-robot-simulation/description/?envType=daily-question&envId=2026-04-06
# 리스트로 in 을 쓰는 것보다, set에 in을 써서 조회하는 게 더 효율적

class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        furthest = 0
        
        pos = [0, 0]
        directions = ['North', 'East', 'South', 'West']
        heading = 0

        obstacles = {tuple(obs) for obs in obstacles}
        

        for command in commands:
            if command == -1:
                heading = (heading + 1) % 4

            elif command == -2:
                heading = (heading - 1) % 4

            else:
                if directions[heading] == 'North':
                    for i in range(command):
                        pos[1] += 1
                        if (pos[0], pos[1]) in obstacles:
                            pos[1] -= 1
                            break

                elif directions[heading] == 'East':
                    for i in range(command):
                        pos[0] += 1
                        if (pos[0], pos[1]) in obstacles:
                            pos[0] -= 1
                            break

                elif directions[heading] == 'South':
                    for i in range(command):
                        pos[1] -= 1
                        if (pos[0], pos[1]) in obstacles:
                            pos[1] += 1
                            break

                else:
                    for i in range(command):
                        pos[0] -= 1
                        if (pos[0], pos[1]) in obstacles:
                            pos[0] += 1
                            break

                distance = pos[0]**2 + pos[1]**2
                furthest = max(furthest, distance)

        return furthest
            
