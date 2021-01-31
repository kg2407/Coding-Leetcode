#https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums, target) :
        dict = {}
        for ind in range(len(nums)):
            complement = target - nums[ind]
            if complement in dict:
                return [dict[complement],ind]
            dict[nums[ind]] = ind