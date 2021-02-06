
def removeDuplicates(S):
    """
    :type S: str
    :rtype: str
    """
 
    duplicates=[]
    for char in S:
        if(S.count(char)>1):
            if(char not in duplicates):
                duplicates.append(char)
    duplicates=set(duplicates)
    for i in duplicates:
        print(i)
        
    return(duplicates)
         
if __name__ == '__main__':
    n = str(input())
    print(removeDuplicates(n))      

return n > 0 and 1162261467 % n == 0