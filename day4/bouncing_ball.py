def bouncing_ball(n,p,k,s,x,y):
    count_x =0
    count_y =0
    max_ =float('+inf')
    for j in range(p+1):
        for i in range(p-1+j,n,k):
            if(int(s[i]) == 0):
                count_x += 1
        a = x*count_x + y*count_y
        count_x =0
        if(a<max_):
            max_ = a

        count_y  +=  1
    print(max_)

def main():
    T=int(input())
    while(T>0):
        n,p,k = [int(i) for i in input().split()]
        s= input()
        x,y =[int(k) for k in input().split()]
        if (len(s)==n):
            bouncing_ball(n,p,k,s,x,y)
        T-=1


if __name__ == "__main__":
    main()