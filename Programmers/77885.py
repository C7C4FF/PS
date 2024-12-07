# https://school.programmers.co.kr/learn/courses/30/lessons/77885
# format(value, 'b') = 2진수 값만, bin(value) = '0b...'
# https://school.programmers.co.kr/questions/37104 참고했음...
# 짝수는 1의 자리가 비어있으니 + 1
# 홀수는 모든 비트가 1이라면 + 1, 가장 작은 0의 위치를 찾고, 해당 자리를 1로 만든 수를 더함. 그리고 그 수를 / 2 한 값을 빼주기
# 100 , 011 은 2배 차이.. 
# ex) 1101 -> 1101 + 10 - 1
# ex) 11011 -> 11011 + 100 - 11

def solution(numbers):
    answer = []
    cnt = 0

    for number in numbers:
        if number % 2 == 0:
            answer.append(number+1)
        else:
            binary_number = format(number, 'b')
            temp = 0
            find_zero = binary_number.rfind('0')

            if find_zero != -1:
                temp = int('0b1' + '0' * (len(binary_number) - find_zero - 1), 2)

            else:
                temp = number + 1

            answer.append(number + temp - temp // 2)

    return answer

'''
시간 초과
def solution(numbers):
    answer = []
    cnt = 0

    for number in numbers:
        binary_number = list(format(number, 'b'))
        next_num = number

        while True:
            cnt = 0
            next_num += 1
            n_list = list(format(next_num, 'b'))

            if len(binary_number) != len(n_list):
                gap = len(n_list) - len(binary_number)
                binary_number = [0] * gap + binary_number

            diff = [origin == added for origin, added in zip(binary_number, n_list)]

            if diff.count(False) <= 2:
                answer.append(next_num)
                break

    return answer
'''
