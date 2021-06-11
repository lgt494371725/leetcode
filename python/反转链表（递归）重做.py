class Solution(object):
    def reverseList(self, head):
        if not head or not head.next: return head
        rev=self.reverseList(head.next)
        head.next.next=head
        head.next=None
        return rev
