/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     public $val = null;
 *     public $left = null;
 *     public $right = null;
 *     function __construct($val = 0, $left = null, $right = null) {
 *         $this->val = $val;
 *         $this->left = $left;
 *         $this->right = $right;
 *     }
 * }
 */
class Solution {

    /**
     * @param TreeNode $root1
     * @param TreeNode $root2
     * @return Boolean
     */
    function getLeaf($root,&$leafArray){
      if($root==null){
          return;
      }
      if($root->left===null && $root->right===null){
        $leafArray[]= $root->val;
       return;
        }
       
         $this->getLeaf($root->left,$leafArray);
         $this->getLeaf($root->right,$leafArray);
      

    }
    function leafSimilar($root1, $root2) {
       
        $root1_arr=[];
        $root2_arr=[];

        $this->getLeaf($root1,$root1_arr);
        $this->getLeaf($root2,$root2_arr);

        return $root1_arr===$root2_arr;

    }
}
