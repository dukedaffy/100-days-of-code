class Solution:
    def isPlaindrome(self, S):
        if(S == S[::-1]):
            return(1)
        else:
            return(0)
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		S = input()
		ob = Solution()
		answer = ob.isPlaindrome(S)
		print(answer)