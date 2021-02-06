
if __name__ == '__main__':
    t = int(input())
    while t > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        k = int(input())
        try:
            print(arr.index(k))
        except:
            print(-1)
        t-=1
