
def one_step(n):

    if( n%2==1):
        x=int((n/2)+1)
        return(2*x*(1+x))
    else:
        return((int(n/2)+1)**2)
  
if __name__ == '__main__':
    n = int(input())
    print(one_step(n))
