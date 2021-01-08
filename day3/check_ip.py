def isValid(string):
    #code here
    flag = False
    
    if ("." in string):
        elements_array = string.strip().split(".")
        if(len(elements_array) == 4 ):
            
            
            for i in elements_array:
                a=len(i)-len(str(int(i)))
                if (i.isnumeric() and len(str(i))<=3 and a == 0 and int(i)>=0 and int(i)<=255):
                    flag=True
                else:
                    break
    return(flag)      
        
if __name__=="__main__":
    t=int(input())
    for _ in range(0,t):
        s=input()
        if(isValid(s)):
            print(1)
        else:
            print(0)