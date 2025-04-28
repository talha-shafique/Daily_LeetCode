class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        for i in range(len(s)):
            if s[i]!=']':
                stack.append(s[i])
            else:
                #Storing alphabets in a string
                st=''
                while stack[-1]!='[':
                    st=stack.pop()+st
                #Discarding [
                stack.pop()
                #Storing the digits
                n=''
                while stack and stack[-1].isdigit():
                    n=stack.pop()+n
                if n=='':
                    n==1
                else:
                    n=int(n)
                res=n*st
                stack.append(res)
        return ''.join(stack)

                





            
        