class Solution(object):
    def findWords(self, words):
        dic1={1:"qwertyuiopQWERTYUIOP",\
        2:"asdfghjklASDFGHJKL",3:"zxcvbnmZXCVBNM"}
        newwords=[]
        for i in words:
            for num in range(1,4):
                if i[0] in dic1[num]:
                    break
            for j in i:
                if j  not in dic1[num]:
                    break
            else: newwords.append(i)
        return newwords
#第二种更好的办法，把键盘每行作为一个集合，如何words的元素都是集合的子集，则说
#明是同一行的
class Solution(object):
    def findWords(self, words):
        set1=set("qwertyuiop")
        set2=set("asdfghjkl")
        set3=set("zxcvbnm")
        return list(filter(lambda word:any(set(word.lower()).issubset(line)\
        for line in [set1,set2,set3]),words))
#这里的列表推导式要会用
