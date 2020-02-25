//Given a singly linked list, determine if it is a palindrome.
package palindrome;
class Solution {
	public boolean isPalindrom(ListNode head) {
		if(head == null || head.next == null) {
			return true;
		}
		ListNode prev = null;
		ListNode slow = head;
		ListNode fast = head;
		while(fast!=null && fast.next!=null){
			fast = fast.next.next;
			ListNode next = slow.next;
			slow.next = prev;
			prev = slow;
			slow = next;
		}
		if(fast!=null) {
			slow = slow.next;
		}
		if (slow.next!=null) {
			if(slow.val!=prev.val){
				return false;
			}
			slow = slow.next;
			prev = prev.next;
		}
		return true;
		}
}
