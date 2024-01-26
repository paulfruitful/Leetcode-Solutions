class Solution {

    /**
     * @param Integer[][] $isConnected
     * @return Integer
     */
  function depth($city, $isConnected, &$visited, $len) {
        $visited[] = $city;
        for ($connected = 0; $connected < $len; $connected++) {
            if (!in_array($connected, $visited) && $isConnected[$city][$connected]){
                    $this->depth($connected, $isConnected, $visited, $len);
                }
            }
        }
    function findCircleNum($isConnected) {
        $visited = [];
        $len = count($isConnected);
        $provinces = 0;

        

        for ($city = 0; $city < $len; $city++) {
            if (!in_array($city, $visited)) {
                $provinces++;
                $this->depth($city, $isConnected, $visited, $len);
            }
        }

        return $provinces;
    }
}
