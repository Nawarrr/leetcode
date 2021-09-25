# Question Link
# https://leetcode.com/problems/design-linked-list/

# Description
'''
Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:

-MyLinkedList() Initializes the MyLinkedList object.
-int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
-void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
-void addAtTail(int val) Append a node of value val as the last element of the linked list.
-void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
-void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.
'''
class ListNode(object):

    def __init__(self, val):
        self.val = val
        self.next = None
        
class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ListNode = ListNode(-1)

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        
        curr = self.ListNode
        for i in range(index+1):
            curr = curr.next
            if curr == None:
                return -1
        return curr.val
        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        newNode = ListNode(val)
        newNode.next = self.ListNode.next
        
        self.ListNode.next =  newNode

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        curr = self.ListNode
        while curr.next:
            curr = curr.next
        curr.next = ListNode(val)

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        curr = self.ListNode
        for i in range(index):
            curr = curr.next
        newNode = ListNode(val)
        next = curr.next
        curr.next = newNode
        newNode.next = next

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        curr = self.ListNode
        for i in range(index):
            curr = curr.next
            if curr == None :
                return
        if curr.next:
            curr.next = curr.next.next

                


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)