def solution(bandage, health, attacks):
    t, x, y = bandage[0], bandage[1], bandage[2]
    timeline = 0
    last = attacks[-1][0]
    ht = 0
    life = health
    
    while timeline <= last:
        if attacks[0][0] == timeline:
            life -= attacks[0][1]
            if life <= 0:
                return -1
            attacks.pop(0)
            ht = 0

        else:
            life += x
            ht += 1
            if ht == t:
                life += y
                ht = 0
            if life >= health:
                life = health

        timeline += 1
        
    return life
