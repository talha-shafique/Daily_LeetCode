class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        temp=''
        for i in range(len(words)):
            temp=temp+words[i]
            print(temp)
            if s==temp:
                return True
        return False

        