# abc 가 모두 최소 한 번씩 등장
# substring 요소가 같더라도, 그 index가 다르면 포함시킴
# len(Counter(substring)) == 3 일 때마다 +1 하기 .. 근데 저번에도 O(n^2)이면 TLE 던데 .. -> TLE
#   -> 반복문을 끝까지 돌리지 말고, len(...) == 3 이 된다면 그 이후로 모든 경우를 더해주고, 반복문을 끝내기
#   -> 그냥 O(n^2) 이면 안 되는 것 같음... sad

# 투포인터 슬라이딩 윈도우로... 똑같이 진행
# len(Counter(substring)) == 3이 될 때까지 진행, 3이 되면 그 이후로의 모든 substring을 더해줌
# 그 뒤에는 왼쪽을 하나씩 옮겨가면서, 여전히 len(...) == 3 이라면 그 이후로의 모든 경우를 더해줌 (n-r)
# 더 이상 abc가 없으면 l을 왼쪽으로 한칸 옮겨서 다시 진행

# Counter() 모듈 변수 앞에 +를 붙이면 0을 제외하고 반환해줌 (와)

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ans = 0
        n = len(s)

        l = 0
        r = 0
        freq = Counter()

        while r < n:
            ch = s[r]
            freq[ch] += 1

            # a,b,c 가 모두 들어가게 됐다면 그 이후의 모든 경우는 'abc가 최소 한번 등장' 조건 만족
            # s의 길이에서 r 포인터을 뺸 값만큼 더함. (r 이후의 모든 글자가 포함됨)
            if len(freq) == 3:
                ans += n - r

                # l 포인터를 오른쪽으로 한칸씩 옮겨보면서 abc가 더 이상 다 들어가지 않을 때까지 반복
                # l 포인터를 하나 옮겨도 여전히 abc가 있다면, r 포인터를 기준으로 그 이하 substring의 값을 더함
                while len(+freq) == 3:
                    l += 1
                    ch = s[l-1]
                    freq[ch] -= 1
                    # +freq 로 0을 제외한 양수 value만 반환함
                    if len(+freq) == 3:
                        ans += n - r
                
                freq = Counter()
                r = l
                continue

            r += 1

        return ans
                    


'''
시간 초과
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        ans = 0
        n = len(s)

        for i in range(n):
            # 초기화
            freq = Counter()
            for j in range(i, n):
                ch = s[j]
                freq[ch] += 1
                # a, b, c가 모두 등장했다면 n-j 로 이하 모든 경우를 포함시킴
                if len(freq) == 3:
                    ans += n-j
                    break
        
        return ans
'''
