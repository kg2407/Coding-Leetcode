#https://leetcode.com/explore/challenge/card/february-leetcoding-challenge-2021/584/week-1-february-1st-february-7th/3625/
class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        # count = 0
        # for _ in range(32):
        #     count += n%2
        #     n //=2
        # return count
        return bin(n).count('1')
        