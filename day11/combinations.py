class Solution(object):
    def combine(self, n,k):
        def dfs(start, combination):
            if len(combination) == k:
                res.append(list(combination))
                return
            
            for i in range(start, n+1):
            
                combination.append(i)
                dfs(i+1, combination)
                combination.pop()
        res = []
        dfs(1, [])
        return res


if __name__=='__main__':
    n=5
    k=3
    ob1=Solution()
    print(ob1.combine(n,k))