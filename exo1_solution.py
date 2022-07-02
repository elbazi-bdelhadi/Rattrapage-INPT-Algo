class Solution(object):
    def buildArray(self, nums):
        L=[]
        for i in range(len(nums)):
            L.append(nums[nums[i]])
        return(L)