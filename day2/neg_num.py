#code
def rearrange(arr, n ) :
 
    
   
    temp = [0 for k in range(n)] 
    
    j = 0 
    for i in range(n): 
        if (arr[i] >= 0 ): 
            temp[j] = arr[i] 
            j +=1
   
    if (j == n or j == 0): 
        return
   
    for i in range(n): 
        if (arr[i] < 0): 
            temp[j] = arr[i] 
            j +=1
    for k in range(n): 
        arr[k] = temp[k] 
            
    return arr
 
# Driver code
k=int(input())
num=[]
for j in range(k):
    n=int(input())
    a = list(map(int,input().strip().split()))[:n]
    if(n>1):
        p=rearrange(a, n)
        num.append(p)
    else:
        num.append(a)
for i in num:
    for j in i:
        print(j,end = " ")
    print()