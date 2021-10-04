/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if (p == null && q == null) return true;
        if (p == null || q == null) return false;
        if (p.val != q.val) return false;
        return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
    }
    
    public boolean isSameTreeWithArrays(TreeNode p, TreeNode q) {
        List<Integer> pTree = new ArrayList<>(); 
        inOrderArray(p, pTree);
        System.out.println("pTree = " + pTree.toString());
        List<Integer> qTree = new ArrayList<>(); 
        inOrderArray(q, qTree);
        System.out.println("qTree = " + qTree.toString());       
        return pTree.equals(qTree);
    }
    
    public List<Integer> inOrderArray(TreeNode t, List<Integer> l) {
        if(t == null) {
            return null;
        }
        l.add(t.val);
        if (t.left == null && t.right != null) l.add(0);
        if(t != null) {
            inOrderArray(t.left, l);        
            inOrderArray(t.right, l);
        }      
        if (t.right == null && t.left != null) l.add(0);
        return l;
    }
}