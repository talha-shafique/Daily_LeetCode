class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        summ=sum(range(0,len(nums)+1))
        return summ-sum(nums)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # Less Efficient Code

        # for i in range(0,len(nums)+1):
        #     if i in nums:
        #         continue
        #     else:
        #         return i
        