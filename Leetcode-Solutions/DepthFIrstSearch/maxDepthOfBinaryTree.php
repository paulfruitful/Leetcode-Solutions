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
     * @param TreeNode $root
     * @return Integer
     */
    
    function maxDepth($root) {
        if($root==null){
           return 0;
        }
        

        $left_depth=$this->maxDepth($root->left);
        $right_depth=$this->maxDepth($root->right);

        return max($left_depth,$right_depth)+1;


        
    }
}
