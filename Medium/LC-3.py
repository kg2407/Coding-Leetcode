#https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        map = {}
        max_len = 0
        start = 0
        if len(s)==0:
            return 0
        for i in range(len(s)):
            if s[i] in map and start <= map[s[i]]:
                start = map[s[i]]+1
            else:
                max_len = max(max_len, i-start+1)
            map[s[i]] = i
        return max_len