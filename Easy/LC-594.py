class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = defaultdict(int)
        ans = 0
        for num in nums:
            dict[(num,num+1)] += 1
            dict[(num-1, num)] += 1
        Set = set(nums)
        
        for k, v in dict.items():
            if k[0] in Set and k[1] in Set:
                ans = max(ans,v)
        return ans
        
        