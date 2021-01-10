def reverseWords(S):
    # code here
    if ("." in s):
        array_ = s.strip().split(".")
        array_[:]= array_[::-1]
        array_='.'.join(array_)
        return(array_)
    else:
        return(s)

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        print(reverseWords(s))

