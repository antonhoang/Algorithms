from typing import List

def climbStairs(self, n: int) -> int:
    a = 1
    b = 0
    for i in range(n):
        a = a + b
        b = a - b
        # a, b = a + b, a
    return a

class Solution:
    def handler(self) -> bool:
        return climbStairs(self, 8)

sol = Solution()
result = sol.handler()
print(result)