class Solution(object):
    def mergeTwoLists(self, l1, l2):
        root=ListNode()
        currentNode=root
        while l1!=None and l2!=None:
            if l1.val<=l2.val:#注意这里，没有必要生成新的节点，直接用原有节点
                currentNode.next,l1=l1,l1.next              
            else:
                currentNode.next,l2=l2,l2.next 
            currentNode=currentNode.next
        if l1==None:
            currentNode.next=l2
        else:
            currentNode.next=l1
        return root.next
