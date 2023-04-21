class Solution {

    /**
     * @param Integer[] $nums1
     * @param Integer $m
     * @param Integer[] $nums2
     * @param Integer $n
     * @return NULL
     */
    function merge(&$nums1, $m, $nums2, $n) {
        $i=0;
        while($i<$m+$n){
            if($i>=$m){
                $nums1[$i]=$nums2[$i-$m];
            }
            $i++;
        }
        sort($nums1);
    }
}
