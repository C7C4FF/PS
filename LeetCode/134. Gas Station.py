# https://leetcode.com/problems/gas-station/description/
# A에서 출발해서 B로 가는 도중 멈췄다면, A-B 사이의 어디서 출발해도 B를 넘지 못함
# circuit_gas = gas + gas, road = circuit_gas[i:i+n+1] 로 사이클을 만들 필요가 없음

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        if sum(gas) < sum(cost):
            return -1

        fuel = 0
        start = 0

        for i in range(n):
            fuel += gas[i] - cost[i]

            if fuel < 0:
                start = i + 1 # i 번째 이전 어디에서 출발해도 다시 갇히기 떄문에, i+1 로 새 스타트하기
                fuel = 0

        return start
