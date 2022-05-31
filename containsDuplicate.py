from typing import List

def containsDuplicate(self, nums: List[int]) -> bool:
    dict = set([])
    for element in nums:
        if element in dict:
            return True
        dict.add(element)
    return False

class Solution:
    def handler(self) -> bool:
        return containsDuplicate(self, [1,2,3,4])

sol = Solution()
result = sol.handler()
print(result)