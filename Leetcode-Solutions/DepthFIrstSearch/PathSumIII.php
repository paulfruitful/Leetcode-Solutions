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
     * @param Integer $targetSum
     * @return Integer
     */
    function pathSum($root, $targetSum) {
        if(!$root){
            return 0;
        }

        return $this->pathCounter($root,$targetSum)+ $this->pathSum($root->left,$targetSum) + $this->pathSum($root->right,$targetSum);
    }

    function pathCounter($root, $targetSum){
          if(!$root){
            return 0;
        }

        $paths=0;

        if($root->val==$targetSum){
            $paths++;
        }

        $paths+=$this->pathCounter($root->left,$targetSum-$root->val);
        $paths+=$this->pathCounter($root->right,$targetSum-$root->val);

        return $paths;


    }
}
