class Solution(object):
    def merge(self,intervals):
        intervals=sorted(intervals,key=self.take_first)
        count=len(intervals)-1
        i=0
        while i < (count):
            if(intervals[i][0]<=intervals[i+1][0] and intervals[i][1]>=intervals[i+1][0]):
                if(intervals[i][1]<=intervals[i+1][1]):
                    intervals[i][1]=intervals[i+1][1]
                
                intervals.pop(i+1)
                count-=1
                i=0
            else:
                i+=1  
        return(intervals)
    def take_first(self,elem):
        return elem[0]
        
        
if __name__ == '__main__':
    intervals=[[2,3],[1,4]]
    print(intervals)
    ob1=Solution()
    print(ob1.merge(intervals))