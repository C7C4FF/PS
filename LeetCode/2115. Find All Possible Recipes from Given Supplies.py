# https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/?envType=daily-question&envId=2025-03-21

# 레시피의 음식이 ingredients로 들어갈 수도 있음. -> bruteforce로 모든 레시피 수만큼 순회하기.
# 레시피의 수만큼 전부 돌면, 순서에 상관 없이 만들 수 있는 음식을 모두 만들 수 있게 됨
# + 리스트로 검사하는 것보다, 집합으로 검사하면 O(1) 시간복잡도를 줄일 수 있음

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        possible = {recipes[i]: ingredients[i] for i in range(len(recipes))}
        supplies = set(supplies)
        ans = set()

        for _ in range(len(recipes)):
            for i in range(len(recipes)):
                # for - else 반복문이 정상적으로 종료되었을 때에만 else 문이 실행됨
                for ingredient in possible[recipes[i]]:
                    if ingredient not in supplies:
                        break
                else:
                    supplies.add(recipes[i])
                    ans.add(recipes[i])
        
        return list(ans)
