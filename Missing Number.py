from typing import List


def missingNumber(self, nums: List[int]) -> int:
    n = len(nums)
    return n * (n + 1) // 2 - sum(nums)

nums = [3,0,1]

class Solution:
    def handler(self):
        return missingNumber(self, nums)

result = Solution()
res = result.handler()
print(res)
