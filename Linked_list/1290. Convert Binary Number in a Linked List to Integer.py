# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        b_n=[]
        curr=head
        while curr:
            a=curr.val
            b_n.append(a)
            print(a)
            curr=curr.next
        d_n=0
        for i in b_n:
            d_n=d_n*2+i
        return d_n    
            

        