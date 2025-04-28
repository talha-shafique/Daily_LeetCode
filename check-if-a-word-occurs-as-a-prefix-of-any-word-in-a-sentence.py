class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        count=[]
        sentence=sentence.split()
        print(sentence)
        for i in sentence:
            print(i)
            if searchWord == i[0:len(searchWord)]:
                count.append(sentence.index(i))
        if count:
            return min(count)+1
        else:
            return -1


        