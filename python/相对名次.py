class Solution(object):
    def findRelativeRanks(self, score):
        score1=score
        score=sorted(score,reverse=True)
        for i in range(1,len(score)+1):
            if i==1:
                score1[score1.index(score[i-1])]='Gold Medal'
            elif i==2:
                score1[score1.index(score[i-1])]='Silver Medal'
            elif i==3:
                score1[score1.index(score[i-1])]='Bronze Medal'
            else:
                score1[score1.index(score[i-1])]=str(i)
        return score1
