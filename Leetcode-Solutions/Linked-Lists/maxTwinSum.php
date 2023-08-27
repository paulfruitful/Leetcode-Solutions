/**
 * Definition for a singly-linked list.
 * class ListNode {
 *     public $val = 0;
 *     public $next = null;
 *     function __construct($val = 0, $next = null) {
 *         $this->val = $val;
 *         $this->next = $next;
 *     }
 * }
 */
class Solution {

    /**
     * @param ListNode $head
     * @return Integer
     */
    function pairSum($head) {

       
        //Convert To Array
        $copy=$head;
        $arr=[];
        while($copy){
           $arr[]=$copy->val;
           $copy=$copy->next;
        }
    
       //Sliding Window Algo

       $maxSum=0;
       $n=count($arr);

       for($i=0; $i<count($arr); $i++){

           $sum=$arr[$i] + $arr[$n-$i-1];

           $maxSum=max($maxSum,$sum);

 
       }

       return $maxSum;
      
       

    }
}
