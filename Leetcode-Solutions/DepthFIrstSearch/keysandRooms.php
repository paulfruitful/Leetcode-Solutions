class Solution {

    /**
     * @param Integer[][] $rooms
     * @return Boolean
     */
      function visitRooms($rooms,$cr,&$visited){
            foreach($rooms[$cr] as $key){
                if(!$visited[$key]){
                    $visited[$key]=true;
                    $this->visitRooms($rooms,$key,$visited);
                }
            }
        }
    function canVisitAllRooms($rooms) {
        $visited=array_fill(0,count($rooms),false);
        $visited[0]=true;

    

        $this->visitRooms($rooms,0,$visited);

        return !in_array(false,$visited);



    }
}
