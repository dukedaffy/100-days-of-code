def occurence(lst,k):
    i,j=0,len(lst)-1
    while i<=j:
        if (lst[i]==k and lst[j]==k):
            return i,j
        elif (lst[i]==k and lst[j]!=k):
            j -= 1
        elif (lst[i]!=k and lst[j]==k):
            i+=1
        else:
            i+=1
            j-=1
if __name__ == '__main__':
    t = int(input())
    while t > 0:
        n,k= map(int, input().split())
        lst = list(map(int, input().strip().split()))
        if k not in lst:
            print(-1)
        else:
            start,end = occurence(lst,k)
            print(start,end,sep=" ")
            
        t-=1