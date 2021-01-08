from collections import Counter
def findDuplicate(nums):
        ldupl = [i for i, cnt in Counter(nums).items() if cnt > 1]
        return ldupl
def main():
    T=int(input())
    while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            final = findDuplicate(arr)
            for i in final:
                print(i,end=" ")
            
            T-=1

if __name__ == "__main__":
    main()
        
