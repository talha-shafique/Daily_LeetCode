class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        # nums.sort(reverse =True)
        # res=[]
        # for i in nums:
        #     dis=abs(i)-0
        #     res.append(dis)
        # return nums[res.index(min(res))]
        nums.sort(reverse =True)
        d={}
        res=0
        for i in nums:
            d[i]=abs(i)-0
        print(d)
        return min(d, key=d.get)






    


        