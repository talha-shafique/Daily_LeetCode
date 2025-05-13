class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l=0
        a=0
        length=len(set(nums))
        for r in range(1,len(nums)):
            if nums[r]==nums[l]:
                continue
            else:
                nums[l+1]=nums[r]
                l=l+1
        return l+1



        

        