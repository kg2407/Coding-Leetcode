# https://leetcode.com/problems/factorial-trailing-zeroes/
class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        div = 5
        while n// div >= 1:
            ans += n//div
            div*=5
        return ans