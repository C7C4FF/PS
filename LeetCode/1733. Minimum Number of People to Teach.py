# 한 언어를 정해서 그 언어를 가르침 -> 모든 친구들이 이어지도록 언어를 가르치기
# 가장 많이 쓰이는 언어를 찾기
# 연결 그래프를 만들기..

class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        langs = [set(l) for l in languages]
        need_teach = set()
        
        for u, v in friendships:
            if langs[u-1] & langs[v-1]:  # 공통 언어 있으면 넘어감
                continue
            need_teach.add(u)
            need_teach.add(v)
        
        if not need_teach:
            return 0  # 이미 다 연결되어 있음
        
        counter = Counter()
        for person in need_teach:
            for lang in langs[person-1]:
                counter[lang] += 1  # 각 언어 등장 횟수 세기
        
        max_known = max(counter.values(), default=0)
        
        # 최소로 가르칠 사람 수 = 전체 후보 - 이미 max_known 언어 아는 사람 수
        return len(need_teach) - max_known
