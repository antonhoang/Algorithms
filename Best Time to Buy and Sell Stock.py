from typing import List

def maxProfit(self, prices: List[int]) -> int:
    maxProfit = 0
    currentPrice = prices[0]
    for i in range(1, len(prices)):
        price = prices[i]
        maxProfit = max(maxProfit, price - currentPrice)
        currentPrice = min(currentPrice, price)
    return maxProfit

class Solution:
    def handler(self) -> int:
        return maxProfit(self, [7,1,5,3,6,4])

sol = Solution()
result = sol.handler()
print(result)