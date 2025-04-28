class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip()
        r=len(s)-1
        word=''
        for i in range(len(s)):
            if s[r].isalnum():
                word=word + s[r]
                r=r-1
            else:
                break
        return len(word)


