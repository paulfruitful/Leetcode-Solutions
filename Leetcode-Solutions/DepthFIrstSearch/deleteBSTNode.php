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
     * @param Integer $key
     * @return TreeNode
     */
    function deleteNode($root, $key) {
        if (!$root){
            return $root;
        }

        if($key>$root->val){
            $root->right=$this->deleteNode($root->right,$key);
        }
        else if($key<$root->val){
            $root->left=$this->deleteNode($root->left,$key);
        }
        else{
            if(!$root->right){
                return $root->left;
            }
            if(!$root->left){
                return $root->right;
            }
            

            $curr=$root->left;
            while ($curr->right){
                $curr=$curr->right;

            } 
            $root->val=$curr->val;
            $root->left=$this->deleteNode($root->left,$curr->val);

        }
        return $root;
    }
}
