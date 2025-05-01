class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        freq={}
        l=0
        for i in range(len(nums)):
            num=nums[i]
            if num not in freq:
                freq[num]=i
            else:
                if abs(i-freq[num])<=k:
                    return True
                else:
                    freq[num]=i
        return False

        
                

        