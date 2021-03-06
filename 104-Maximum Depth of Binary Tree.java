//104. Maximum Depth of Binary Tree

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
 
//DFS with recursion 
class Solution {
  
    public int maxDepth(TreeNode root) {
        
        if(root == null){
            return 0;
        }
        if(root.left == null && root.right == null){
        
            return 1;
            
        }

        
        return 1 + Math.max(maxDepth(root.left), maxDepth(root.right));
    }
}

//DFS without recursion


//BFS without recursion