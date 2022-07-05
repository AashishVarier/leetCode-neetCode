//21. Merge Two Sorted Lists
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
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) { //l1 and l2 represent the reference address of the head
        
        ListNode dummyList = new ListNode();
        ListNode cur = dummyList; //avoid edge case of inserting into empty list
          
        while(l1 != null & l2 != null){ //compare both LinkedList node till either of their  node reference is null && append the smaller node reference  to dummyList as its next node
            if(l1.val < l2.val){
               cur.next = l1;
               l1 = l1.next;
            }
            else {
                cur.next = l2;
                l2 = l2.next;
            }
            
            cur = cur.next;
        }
      //total number of node in L2 might be more than L1 ,append the  L2 reference after while() as dummyList next or vice versa. 
	  //OR L1 / L2 could be both null or either one null - so wont enter while() loop
	 
       if(l1 == null){
            cur.next = l2;
        }
        else if(l2 == null){
            cur.next =  l1;
        }

        return dummyList.next;

    }
    
}