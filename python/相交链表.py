class Solution(object):
    def getIntersectionNode(self, headA, headB):
        numA,numB=1,1
        currentA,currentB=headA,headB
        while currentA!=None and currentB!=None:
            if currentA==currentB:
                return currentA
            currentA=currentA.next
            currentB=currentB.next
            if currentA==None and numA:
                currentA=headB
                numA-=1
            if currentB==None and numB:
                currentB=headA
                numB-=1
        return None
