#User function Template for python3
class Solution:

    def maxProduct(self,arr, n):
        # code here
        result = arr[0] 
        for i in range(n):
            mul = arr[i]
            for j in range(i + 1, n):
                result = max(result, mul)
                mul *= arr[j]
            result = max(result, mul)
        return result


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxProduct(arr, n)
        print(ans)
        tc-=1