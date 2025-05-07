class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        bc=2**k
        temp=set()
        for i in range(len(s)):
            ss=s[i:i+k]
            if len(ss)==k:
                temp.add(ss)
        if len(temp)==bc:
            return True
        else:
            return False
            
           

            



        