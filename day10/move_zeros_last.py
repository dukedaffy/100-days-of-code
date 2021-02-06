class Solution(object):
    def moveZeroes(self, nums):
        count=0
        count1=0
        for i in range(len(nums)):
            if(nums[i]==0):
                count+=1
            else:
                nums[count1]=nums[i]
                count1+=1
        for i in range(count):
            nums[len(nums)-i-1]=0
                
        return(nums)

if __name__ == '__main__':
    nums=[1,0,2,2,0,5]
    ob1=Solution()
    print(ob1.moveZeroes(nums))