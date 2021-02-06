class Solution(object):
    def isPossibleDivide(self, nums, k):
        if len(nums)%k != 0:
            return False
        # move list -> multiset
        counter = {}
        for num in sorted(nums):
            if num in counter:
                counter[num] = counter[num] + 1
                #print('1',num,counter)
                
            else:
                
                counter[num] = 1
                #print('2',num,counter)
        # group numbers into groups of k
        while counter:
            # get next min
            next_num = next(iter(counter))
            for next_num in range(next_num, next_num + k):
                # consecutive number not present
                if next_num not in counter:
                    return False
                counter[next_num] = counter[next_num] - 1
                # remove depleted numbers
                if not counter[next_num]:
                    del(counter[next_num])
        
        return True

        
if __name__=="__main__":
    nums =[3,2,1,2,3,4,3,4,5,9,10,11]
    k=3
    print(nums)
    ob1=Solution()
    ans=ob1.isPossibleDivide(nums,k)
    print(ans)
    