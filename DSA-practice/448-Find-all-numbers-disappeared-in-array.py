# Failed Solution (Due to exceeding time limit)
#because of the nested loop, the time complexity is O(n^2)
class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        a=[]
        for i in range(1,len(nums)+1):
            if i not in nums:
                a.append(i)
        return a

#Correct Solution
# we try to make a single n loop solution, so that the time complexity is O(n)
class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        num_set=set(nums)
        return[i for i in range(1,len(nums)+1) if i not in num_set]