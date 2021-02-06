#https://leetcode.com/problems/reverse-string/
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        start = 0
        end = len(s)-1
        while start < end:
            temp = s[start]
            s[start] = s[end]
            s[end] = temp
            start += 1
            end -= 1
        return s
        
        # for i in range(int(len(s)/2)):
        #     first_char = s[i]
        #     s[i] = s[len(s) - i - 1]
        #     s[len(s) - i - 1] = first_char