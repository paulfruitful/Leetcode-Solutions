class Solution {

    /**
     * @param Integer $city
     * @param Integer $changes
     * @param array $neighbours
     * @param array $connections
     * @param array $visited
     */
    private function dfs($city, &$changes, &$neighbours, &$connections, &$visited) {
        foreach ($neighbours[$city] as $neighbour) {
            if (!isset($visited[$neighbour])) {
                $visited[$neighbour] = true;

                if (!isset($connections[$neighbour][$city])) {
                    $changes++;
                }

                $this->dfs($neighbour, $changes, $neighbours, $connections, $visited);
            }
        }
    }
[1] [0,2] [1,3] [2,4] [3]
[1][0]=true
0,1=true
[1],3=true
    /**
     * @param Integer $n
     * @param Integer[][] $connections
     * @return Integer
     */
    function minReorder($n, $connections) {
        $neighbours = array_fill(0, $n, []);
        $connectionsMap = [];

        foreach ($connections as [$a, $b]) {
            $neighbours[$a][] = $b;
            $neighbours[$b][] = $a;
            $connectionsMap[$a][$b] = true;
        }

        $visited = [0 => true];
        $changes = 0;
        $this->dfs(0, $changes, $neighbours, $connectionsMap, $visited);

        return $changes;
    }
}
