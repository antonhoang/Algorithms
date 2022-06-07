from typing import List


def maxSubArray(self, nums: List[int]) -> int:
    maxSum = nums[0]
    currentSum = nums[0]
    for i in range(1, len(nums)):
        num = nums[i]
        currentSum = max(currentSum + num, num)
        maxSum = max(currentSum, maxSum)
    return  maxSum


class Solution:
    def handler(self) -> bool:
        return maxSubArray(self, [-2,1,-3,4,-1,2,1,-5,4])

sol = Solution()
result = sol.handler()
print(result)


