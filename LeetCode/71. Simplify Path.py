# https://leetcode.com/problems/simplify-path/description/

class Solution:
    def simplifyPath(self, path: str) -> str:
        ans = ""
        
        dir_and_file = []

        name = []
        cnt = 0
        for ch in path:
            if ch == ".":
                cnt += 1
            elif cnt == 1 and ch == "/" and not name:
                cnt = 0
            elif cnt == 2 and ch == "/" and not name:
                if dir_and_file:
                    dir_and_file.pop()
                cnt = 0
            elif cnt > 0 and ch == "/" and name:
                name.append("."*cnt)
                cnt = 0
            elif cnt > 2 and ch == "/":
                dir_and_file.append("."*cnt)
                cnt = 0
            elif cnt > 0 and ch.isalpha():
                name.append("."*cnt)
                cnt = 0

            if ch.isalpha() or (ch != "." and ch != "/"):
                name.append(ch)
            elif not ch.isalpha() and ch != "." and name:
                dir_and_file.append("".join(name))
                name = []
                
        
        if cnt == 2 and not name:
            if dir_and_file:
                dir_and_file.pop()
        elif cnt > 0 and name:
            name.append("."*cnt)
        if cnt > 2:
            dir_and_file.append("."*cnt)
            
        if name:
            dir_and_file.append("".join(name))

        for n in dir_and_file:
            ans += f"/{n}"

        if ans == "":
            return "/"
        else:
            return ans
        

        
        
        
