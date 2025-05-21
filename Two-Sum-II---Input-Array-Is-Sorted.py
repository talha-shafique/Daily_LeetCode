class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=0
        r=len(numbers)-1
        res=0
        while r>l:
            res=numbers[l]+numbers[r]
            if res>target:
                r=r-1
            elif res<target:
                l=l+1
            else:
                return l+1,r+1
            
        