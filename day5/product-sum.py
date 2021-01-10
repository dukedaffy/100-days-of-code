class Solution(object):
    def subtractProductAndSum(self, n):
        """
        :type n: int
        :rtype: int
        """
        sum = 0
        pro=1
        for digit in str(n):   
            sum += int(digit)
            pro *= int(digit)
        return (pro-sum)
        
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        ob = Solution()
        ans = ob.subtractProductAndSum(n)
        print(ans)
        tc-=1