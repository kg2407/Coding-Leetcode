#https://leetcode.com/problems/palindrome-number/
class Solution:
    def isPalindrome(self, x: int) :
        x = str(x)
        if x == x[::-1]:
            return True
        return False