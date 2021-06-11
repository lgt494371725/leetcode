class Solution(object):
    def addTwoNumbers(self, l1, l2):
        root=ListNode()
        l3=root
        carry=0
        while l1!=None and l2!=None:
            if carry:
                value=(l1.val+l2.val+1)%10 #每个节点数字都是0-9，预防出现10的情况
            else:
                value=(l1.val+l2.val)%10
            carry=1 if l1.val+l2.val+carry>=10 else 0#或者直接sum/10
            l4=ListNode(value)
            l3.next=l4
            l3=l4
            l1=l1.next
            l2=l2.next
        if l1!=None:
            l3.next=l1
            while (carry+l1.val)/10 and l1.next!=None:
                carry=(l1.val+1)/10 #注意顺序，先判断carry，再改变值
                l1.val=(l1.val+1)%10
                l1=l1.next
            if (l1.val+carry)/10:
                l1.next=ListNode(1)
            l1.val=(l1.val+carry)%10
        elif l2!=None:
            l3.next=l2
            while (carry+l2.val)/10 and l2.next!=None:
                carry=(l2.val+1)/10
                l2.val=(l2.val+1)%10
                l2=l2.next
            if (l2.val+carry)/10:
                l2.next=ListNode(1)
            l2.val=(l2.val+carry)%10
        else:
            if carry:
                l3.next=ListNode(1)
        return root.next
#简洁的写法
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry=0
        head=tail=ListNode()
        while l1!=None or l2!=None:
            n1=l1.val if l1 else 0
            n2=l2.val if l2 else 0
            sum1=n1+n2+carry
            tail.next=ListNode(sum1%10)
            tail=tail.next
            carry=sum1//10
            if l1!=None:
                l1=l1.next
            if l2!=None:
                l2=l2.next
        if carry>0:
            tail.next=ListNode(carry)
        return head.next
































        
