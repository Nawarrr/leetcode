//Question Link
//https://leetcode.com/problems/binary-tree-inorder-traversal/

// Given the root of a binary tree, return the inorder traversal of its nodes' values.

 
/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[]}
 */

 var inorderTraversal = function(root , output = []) {

    if (root == null){
        return output }
    inorderTraversal(root.left , output)
    output.push(root.val)
    inorderTraversal(root.right , output)
    

    return output
};