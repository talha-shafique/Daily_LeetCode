class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        s=set()
        for i in nums:
            if i in s:
                s.remove(i)
            else:
                s.add(i)
        return s.pop()


        
        
        
        
        
        
        
        
        
        
        
        
        
        #Less Efficient
        # for i in nums:
        #     if nums.count(i)==1:
        #         return i

        