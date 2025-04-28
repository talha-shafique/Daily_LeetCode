class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:

        for i in range(len(arr)):
            if 2*arr[i] in arr[0:i]+arr[i+1:]:
                print(arr[i])
                return True
        return False

            
        # arr.sort(reverse=True)
        # print(arr)
        
        # for r in range(len(arr)):
        #     l=len(arr)-1
        #     while l>r:
        #         if 2*arr[l]==arr[r]:
        #             return True
        #         else:
        #             l=l-1
        # return False
        