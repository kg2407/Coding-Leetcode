#https://leetcode.com/contest/biweekly-contest-44/problems/find-the-highest-altitude/
class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        max = 0
        temp = 0
        for num in gain:
            temp += num
            if (max < temp):
                max = temp
        return max