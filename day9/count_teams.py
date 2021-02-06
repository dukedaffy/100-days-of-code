class Solution(object):
    def numTeams(self, rating):
        
        smf = [] 
        bgf = [] 
        for i in range(len(rating)):
            bg = 0
            sm = 0
            for j in range(i+1, len(rating)):
                if rating[i] > rating[j]:
                    sm += 1
                if rating[i] < rating[j]:
                    bg += 1
            smf.append(sm)
            bgf.append(bg)
        
        ans = 0
        for i in range(len(rating)):
            for j in range(i+1, len(rating)):
                if rating[i] > rating[j]:
                    ans += smf[j]
                if rating[i] < rating[j]:
                    ans += bgf[j]
        return ans
        
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.numTeams(arr)
        print(ans)
        tc-=1