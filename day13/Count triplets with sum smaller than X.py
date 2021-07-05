def findTriplets(lst, k): 
    triplet_count = 0
    final_temp_list =[] 
    loop_cnt=0
      
    for i in range(0, len(lst)-1):  
        loop_cnt+=1
          
        s = set()  
        temp_list = [] 
  
        # Adding first element 
        temp_list.append(lst[i]) 
  
        curr_k = k - lst[i]  
          
        for j in range(i + 1, len(lst)-1):  
            a =  curr_k - lst[j]
            temp_list.append(lst[j])
            for k in range(j+1,len(lst)-1):
                
                if (lst[k] < a):
                     
                    temp_list.append(lst[k]) 
                    triplet_count += 1
                    print(temp_list)
                    final_temp_list.append(tuple(temp_list)) 
                    temp_list.pop(2) 

                
                
            temp_list.pop(1) 
            s.add(lst[j]) 
   
    print(loop_cnt)          
    return final_temp_list,triplet_count

# Driver Code 
lst = [5,1,3,4,7] 
k = 12
print(findTriplets(lst, k)) 