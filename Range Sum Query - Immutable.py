from typing import List


class NumArray:

    def __init__(self, nums: List[int]):
        sums = []
        currentNum = 0
        for i in nums:
            currentNum += i
            sums.append(currentNum)
        self.sums = sums

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.sums[right]
        else:
            return self.sums[right] - self.sums[left - 1]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)