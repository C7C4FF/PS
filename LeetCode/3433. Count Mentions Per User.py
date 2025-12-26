# https://leetcode.com/problems/count-mentions-per-user/description/?envType=daily-question&envId=2025-12-12

class Solution:
    def countMentions(self, numberOfUsers: int, events: List[List[str]]) -> List[int]:
        sorted_events = sorted(events, key = lambda x: (int(x[1]), x[0] != "OFFLINE"))
        off = [-1] * numberOfUsers
        on = [0] * numberOfUsers
        cnt_all = 0

        for task, stamp, ids in sorted_events:
            now = int(stamp)
            ids_cnt = Counter(ids.split())

            for i in range(numberOfUsers):
                if now >= off[i]:
                    off[i] = -1

            if task == "MESSAGE":
                if ids_cnt.get("HERE", 0):
                    for id in range(numberOfUsers):
                        if off[id] == -1:
                            on[id] += ids_cnt["HERE"]

                if ids_cnt.get("ALL", 0):
                    cnt_all += ids_cnt["ALL"]
                
                for uid, cnt in ids_cnt.items():
                    if uid == "ALL" or uid == "HERE":
                        continue
                    id = int(uid[2:])
                    on[id] += cnt

            elif task == "OFFLINE":
                for user in ids_cnt:
                    uid = int(user)
                    off[uid] = now + 60

        for i in range(numberOfUsers):
            on[i] += cnt_all

        return on
