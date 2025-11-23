# 플레이어는 트레이너보다 낮아야 함
# 트레이너는 하나의 플레이어만 담당 가능
# 둘 다 정렬하고

class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        
        i = 0
        matched = 0
        n = len(trainers)


        for player in players:
            # 현재 trainers[i]가 player보다 작으면, 다음 트레이너를 살펴본다
            while i < n and trainers[i] < player:
                i += 1
            
            if i == n:
                break
            
            matched += 1
            i += 1  # 이 트레이너는 이제 사용했으니 포인터 올려주기
    
        return matched
