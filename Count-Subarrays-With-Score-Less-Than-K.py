class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        l=0
        score=0
        win=0
        count=0
        for r in range(len(nums)):
            score+=nums[r]
            win=r-l+1
            while score*win>=k:
                score-=nums[l]
                l=l+1
                win-=1
            if score*win<k:
                count+=win
        return count

        