# https://leetcode.com/problems/add-two-numbers/
# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single digit. 
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,head ):
        if head ==None:
            return None
        prev = None
        curr= head
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev

    def ll_to_int(self, head):
        if head == None:
            return 0
        num = ""
        while head:
            num+=str(head.val)
            head = head.next
        num = int(num)
        return num

    def int_to_ll(self, num):
        
        new_node = ListNode()
        node = new_node
        for n in num:
            node.next = ListNode(int(n))
            node = node.next
        return new_node.next

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l1_rev = self.reverse(l1)
        l2_rev = self.reverse(l2)
        num1 = self.ll_to_int(l1_rev)
        num2 = self.ll_to_int(l2_rev)
        num3 = num1+num2
        num3 = str(num3)
        num3 = num3[::-1]
        node = self.int_to_ll(num3)
        return node