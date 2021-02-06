class Solution(object):
    def method1(self, n):
        return n > 0 and 1162261467 % n == 0
    
    def method2(self,n):
        i = 1
        while (i < n):
            i *= 3
        
        return True if n == i else False

if __name__ == '__main__':
    n=127
    ob1=Solution()
    print("method 1-",ob1.method1(n))
    print("method 2-",ob1.method2(n))