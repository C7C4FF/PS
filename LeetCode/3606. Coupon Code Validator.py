# https://leetcode.com/problems/coupon-code-validator/description/?envType=daily-question&envId=2025-12-13

class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        n = len(code)
        business = ["electronics", "grocery", "pharmacy", "restaurant"]
        ans = []

        for c, b, a in zip(code, businessLine, isActive):
            
            if (re.fullmatch(r'\w+', c) is not None) and (b in business) and a:
                ans.append((c, b))
        
        sorted_ans = sorted(ans, key = lambda x: (x[1], x[0]))
        ans = [c for c, _ in sorted_ans]

        return ans
