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

import java.math.BigInteger;
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int carry = 0, i = 0, j = 0;
        ListNode head = new ListNode(0);
        ListNode curr = head;
        while(l1 != null || l2 != null || carry != 0) {
            if(l1 != null) {
                System.out.println("l1[" + i + "] = before(carry = " + carry + ")");
                carry += l1.val;
                System.out.println("l1[" + i + "] = after(carry = " + carry + ")");
                l1 = l1.next;
                i++;
            }
            if(l2 != null) {
                System.out.println("l2[" + j + "] = before(carry = " + carry + ")");
                carry += l2.val;
                System.out.println("l2[" + j + "] = after(carry = " + carry + ")");
                l2 = l2.next;
                j++;
            }
            curr.val = carry%10;
            if(l1 == null && l2 == null && carry / 10 == 0) {
                break;
            }
            curr.next = new ListNode();
            System.out.println("35: carry: " + carry);
            carry /= 10;
            System.out.println("37: carry: " + carry);
            curr = curr.next;
        }
        return head;
    }

}

/* Bad Solution    
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        System.out.println("start");
        BigInteger num0 = new BigInteger(BigInteger.valueOf(parse(l1)));
        System.out.println("num0 = " + num0);
        int num1 = new BigInteger('0');
            parse(l2);
        System.out.println("num1 = " + num1);
        int num2 = num0 + num1;
        System.out.println("sum = " + num2);
        return convert(num2);
    }
    
    public String parse(ListNode l) {
        Stack<Long> stack = new Stack<>();
        StringBuilder sb = new StringBuilder(); 
        stack.push((long) l.val);
        System.out.println("l.val = " + (long) l.val);
        ListNode curr = l;
        
        while(curr.next != null) {
            stack.push((long) curr.next.val);
            System.out.println("curr.next.val = " + (long) curr.next.val);
            curr = curr.next;
        }
        
        while(stack.empty() == false) {
            sb.append(stack.pop());
            System.out.println("sb = " + sb.toString());
        }
        
        return sb.toString();
    }
    
    public ListNode convert(long n) {
        String num = String.valueOf(n);
        Stack<Long> stack = new Stack();
        ListNode l3 = new ListNode();
        ListNode ll = l3;
        for(int i = 0; i < num.length(); i++){
            stack.push((long) Character.getNumericValue(num.charAt(i)));
        }
        
        while(stack.empty() == false) {
            ll.val = stack.pop().intValue();
            if (stack.empty() == true)
                break;
            ll.next = new ListNode();
            ll = ll.next;
        }
        return l3;
    }
*/