#https://leetcode.com/problems/fizz-buzz/
class Solution:
    
    def fizzBuzz(self, n: int) :
        ans = []
        for num in range(1,n+1):
            if num%15 ==0:
                ans.append('FizzBuzz')
            elif num%3 ==0:
                ans.append('Fizz')
            elif num%5 == 0:
                ans.append('Buzz')
            else:
                ans.append(str(num))
        return ans