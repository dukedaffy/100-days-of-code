def check_anagram(s,t):
    if( sorted(s)==sorted(t)):
        print("True")
    else:
        print("false")

if __name__ == '__main__':
    n,k = [str(k) for k in input().split()]
    check_anagram(n,k)