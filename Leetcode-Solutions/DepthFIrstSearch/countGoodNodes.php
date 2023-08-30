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
    function getGoodNodes($root,&$goodNodes,$prevNode){
        if($root==null){
            return;
        }
        if ($root->val>=$prevNode){
           $goodNodes[]=$root->val;
        }

        $this->getGoodNodes($root->right,$goodNodes,max($root->val,$prevNode));
        $this->getGoodNodes($root->left,$goodNodes,max($root->val,$prevNode));
        
    }
    function goodNodes($root) {
        $goodNodes=[];
        $this->getGoodNodes($root,$goodNodes,PHP_INT_MIN);
        return count($goodNodes);
    }
}
