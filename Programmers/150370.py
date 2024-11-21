import datetime as dt
from dateutil.relativedelta import relativedelta

def solution(today, terms, privacies):
    answer = []
    todaydt = dt.datetime.strptime(today, "%Y.%m.%d")
    
    for i in range(1, len(privacies)+1):
        temp = privacies[i-1].split(' ')
        time = dt.datetime.strptime(temp[0], "%Y.%m.%d")
        term = temp[1]
        
        for j in terms:
            temp0 = j.split(' ')
            if temp0[0] == term:
                time += relativedelta(months=int(temp0[-1]))
                if todaydt >= time:
                    answer.append(i)
                
                      
    return answer
