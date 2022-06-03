from typing import List

def singleNumber(self, nums: List[int]) -> int:
    mask = 0
    for element in nums:
        mask ^= element  ##XOR
    return mask

class Solution:
    def handler(self) -> int:
        return singleNumber(self, [4,1,2,1,2])

sol = Solution().handler()
print(sol)

#alternative resolve
def singleNumber2(self, nums: List[int]) -> int:
    seen = set()
    s = 0
    for num in nums:
        if num in seen:
          s -= num
        else:
          s += num
          seen.add(num)
    return s

sol2 = Solution().handler()
print(sol2)