from typing import List

def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
    i = 0
    while i < len(nums):
        pos = nums[i] - 1
        if nums[i] != nums[pos]:
            nums[i], nums[pos] = nums[pos], nums[i]
        else:
            i += 1
    miss = []
    for i in range(len(nums)):
        if nums[i] != i + 1:
            miss.append(i + 1)
    return miss

class Solution:
    def handler(self):
        return findDisappearedNumbers(self, [4,3,2,7,8,2,3,1])

result = Solution()
res = result.handler()
print(res)