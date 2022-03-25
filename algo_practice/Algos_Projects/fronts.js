class Node {
    constructor(data) {
        this.data = data;
        this.next = null;              
    }
}
class SLL {
    constructor() {
        this.head = null;
    }
    addFront(val) {
        // Creating a new node object with the value provided
        let new_node = new Node(val);
        new_node.next = this.head // connects the new node to the list 
        this.head = new_node // Move the head of the list to this noce
        console.log(this)
        return this.head
        }
    remove_front() {
        if (this.head == null) {
            return this.head;
        }
        var removedNode = this.head;
        this.head = removedNode.next;
        removedNode.next = null;
        console.log(this.head)
        return this.head
    }
    return_front(){
        if (this.head == null){
            console.log(this.head)
            return this.head;
        } else {
            console.log(this.head.value)
            return this.head.value;
        }
    }
    } 
    
var my_list = new SLL
console.log(my_list)
my_list.addFront(4)
my_list.addFront(5)
my_list.addFront(2)
my_list.addFront(7)
my_list.remove_front()
my_list.return_front()
