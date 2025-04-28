class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i in range(len(nums)):
            if target in nums:
                return nums.index(target)
            else:
                nums.append(target)
                nums.sort()
                return nums.index(target)
        