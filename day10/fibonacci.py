class Solution(object):
    def fib(self, n):
        if (n == 0 or n == 1):
            return n
        
        a, b = 0, 1
        for _ in range(n-2):
            a, b = b, a + b
        return(b)
        
if __name__ == '__main__':
    n=5
    ob1=Solution()
    ans=ob1.fib(5)
    print(ans)