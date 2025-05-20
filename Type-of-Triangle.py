class Solution:
    def triangleType(self, nums: List[int]) -> str:
        freq={}
        if nums[0] + nums[1] <= nums[2] or nums[0] + nums[2] <= nums[1] or nums[1] + nums[2] <= nums[0]:
            return 'none'
        for i in range(len(nums)):
            if nums[i] in freq:
                freq[nums[i]]+=1
            else:
                freq[nums[i]]=1
        if len(freq)==1:
            return 'equilateral'
        elif len(freq)==2:
            return 'isosceles'
        else:
            return 'scalene'