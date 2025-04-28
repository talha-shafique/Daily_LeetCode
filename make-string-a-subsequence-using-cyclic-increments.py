class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        p=0
        res=''
        if len(str1)<len(str2):
            return False
        else:
            for i in str1:
                while p<len(str2):
                    if i=='z' and str2[p]=='a':
                        res=res+str2[p]; p=p+1
                        break
                    elif i==str2[p] or ord(i)+1==ord(str2[p]):
                        res=res+str2[p]; p=p+1
                        break
                    else:
                        break
        return res==str2

        

        
        

        

        