# https://leetcode.com/problems/shortest-distance-to-a-character/

class Solution(object):
    def shortestToChar(self, s, c):
        """
        :type s: str
        :type c: str
        :rtype: List[int]
        """
        N = len(s)
        left, right, output = [None]*N, [None]*N, [None]*N
        temp = float('inf')
        
        for i in range(N):
            if s[i] == c:
                temp = 0
            left[i] = temp
            temp +=1
        for i in range(N-1, -1, -1):
            if s[i] == c:
                temp = 0
            right[i] = temp
            temp += 1
        for i in range(N):
            if left[i] <= right [i]:
                output[i] = left[i]
            else:
                output[i] = right[i]
        return output