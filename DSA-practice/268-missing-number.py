#solution 1st try
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        for i in range(len(nums)+1):
            if i not in nums:
                return i
#solution 2
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n=len(nums)
        return n*(n+1)//2-sum(nums)
