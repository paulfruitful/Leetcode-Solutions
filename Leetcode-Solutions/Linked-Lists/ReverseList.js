
var reverseList = function(head) {
    let prev=null
    let current= head

    while(current){
        let next_node=current.next
        current.next=prev
        prev= current
        current=next_node
    }

    return prev
};
