def kthSmallest(mat, n, k): 
    a = sum(mat, []) 
    a.sort()
    return(a[k-1])




if __name__=="__main__":
    T=int(input()) #number of test case
    while(T>0):
        n = int(input()) #number of rows and column (square matrix)
        mat=[[0 for j in range(n)] for i in range(n)] #initializing zero matrix
        line1=[int(x) for x in input().strip().split()] #elements in matrix- type by leaving a space
        k = int(input()) #kth smallest element

        temp=0
        for i in range(n):
            for j in range (n):
                mat[i][j]=line1[temp]
                temp+=1
        
        print(kthSmallest(mat, n, k))
        T-=1
    