class Solution {

    /**
     * @param Integer[] $gain
     * @return Integer
     */
    function largestAltitude($gain) {
        $highest=0;
        $sum=0;
        foreach($gain as $x){
            $sum+=$x;
            $highest=max($highest,$sum);
        }
        
        return $highest;
    }
}
