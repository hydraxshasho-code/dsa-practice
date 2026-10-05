#solution 1st try
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        for i in range(len(nums)+1):
            if i not in nums:
                return i

#solution 2nd try
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        return (n * (n + 1)) // 2 - sum(nums)
    
#college solutions
class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n=len(nums)
        expected_sum=n*(n+1)//2
        actual_sum=0
        for x in nums:
            actual_sum+=x
        missing=expected_sum-actual_sum
        return missing
        