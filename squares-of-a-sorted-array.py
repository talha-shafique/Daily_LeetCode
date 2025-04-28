class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # return sorted([x**2 for x in nums])
        res=[]
        for i in nums:
            i=i**2
            res.append(i)
        res.sort()
        return res
        