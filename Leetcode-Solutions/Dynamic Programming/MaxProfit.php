
class Solution {

    /**
     * @param Integer[] $prices
     * @return Integer
     */
    function maxProfit($prices) {
        $max_profit = 0;
        $min_price = PHP_INT_MAX;

        for ($i = 0; $i < count($prices); $i++) {
            $min_price = min($min_price, $prices[$i]); 
            $current_profit = $prices[$i] - $min_price; 
            $max_profit = max($max_profit, $current_profit); 
        }

        return $max_profit;
    }
}
