class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        while original in nums:
            original =2*original
        return original
        
        
        
        
        
        
        
        
        
        
        
        #Less Efficient Solution
        # for i in nums:
        #     if original in nums:
        #         original=2*original
        # return original