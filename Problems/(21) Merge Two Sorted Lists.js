//Question Link
//https://leetcode.com/problems/merge-two-sorted-lists/
/*
 Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists. 
 */

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var mergeTwoLists = function(l1, l2) {
    let list1 = new ListNode
    let start = list1
    while (l1 && l2) {
        if (l1.val < l2.val ){
            list1.next = l1
            l1 = l1.next    
    }   else {
            list1.next = l2
            l2 = l2.next
    }   list1 = list1.next
        
    } list1.next = l1 ? l1 : l2 
    
    return start.next
    
            
            
         
    
};
