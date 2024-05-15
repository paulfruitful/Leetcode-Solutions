class Solution {

    /**
     * @param String[][] $maze
     * @param Integer[] $entrance
     * @return Integer
     */
    function nearestExit($maze, $entrance) {
        $rows=count($maze);
        $cols=count($maze[0]);
        $queue=[[$entrance[0],$entrance[1],-1]];

        while($queue){
            list($r, $c, $d) = array_shift($queue); 
            if ($r < 0 || $r >= $rows || $c < 0 || $c >= $cols){
                if($d>0){
                    return $d;
                }
                continue;
            }

            if($maze[$r][$c]=='+'){
                continue;
            }
            $maze[$r][$c]='+';
            $moves = [[0,1],[0,-1],[1,0],[-1,0]];

           foreach($moves as $move) {
                $f = $move[0];
                $b = $move[1];

                $queue[]=[$r+$f,$c+$b,$d+1];
            }

        }

        return -1;

    }
}
