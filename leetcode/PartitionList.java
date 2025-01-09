// platform: leetcode - https://leetcode.com/problems/partition-list/
// programming language: Java
// status: Accepted

// author: Gabriel Soares
// https://www.linkedin.com/in/gabrielsoarespebr/
// https://github.com/gabrielsoarespebr

/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode partition(ListNode head, int x) {
        if (head == null) return head;
        if (head.next == null) return head;
        
        ListNode headLessThan = new ListNode(0);
        ListNode headGreaterThan = new ListNode(0);
        
        ListNode lessThan = headLessThan;
        ListNode greaterThan = headGreaterThan;
        
        ListNode temp = head;
        
        while (temp != null){
            if (temp.val < x){
                lessThan.next = temp;
                
                lessThan = temp;
            } else{
                greaterThan.next = temp;
                
                greaterThan = temp;
            }
            
            temp = temp.next;
        }
        
        headLessThan = headLessThan.next;
        headGreaterThan = headGreaterThan.next;
        
        lessThan.next = headGreaterThan;
        
        if (greaterThan != null) greaterThan.next = null;
        
        if (headLessThan == null){ 
            head = headGreaterThan;
        } else {
            head = headLessThan;
        }
        
        return head;
    }
}