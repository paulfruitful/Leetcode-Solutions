class Solution {

    /**
     * @param TreeNode $root
     * @return Integer
     */

    function helper($root, $direction, $currLength, &$maxLength) {
        if (!$root) {
            return;
        }

        $maxLength[0] = max($maxLength[0], $currLength);

        if ($direction == "right") {
            $this->helper($root->left, 'left', $currLength + 1, $maxLength);
            $this->helper($root->right, 'right', 1, $maxLength);
        } else {
            $this->helper($root->right, 'right', $currLength + 1, $maxLength);
            $this->helper($root->left, 'left', 1, $maxLength);
        }
    }

    function longestZigZag($root) {
        $maxLength = [0];
        $this->helper($root, 'right', 0, $maxLength);
        $this->helper($root, 'left', 0, $maxLength);
        return $maxLength[0];
    }
}
