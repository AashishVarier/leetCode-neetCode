//155. Min Stack

class MinStack {

    private Node top;
    
    public MinStack() {
        
    }
    
    public void push(int val) {
        if(top == null){ //no element in Node
            top = new Node(val, val, null);
        }
        else{
            top = new Node(val, Math.min(val, top.minimum), top);
        }
        
    }
    
    public void pop() {
        top = top.next; 
    }
    
    public int top() {
        return top.value;
    }
    
    public int getMin() {
        return top.minimum;
    }
    
    private class Node {
        int value; //value to be stored
        int minimum; //minimum value 
        Node next; //refernce of next node (becuase java doesn't use pointer)
        
        private Node (int value, int minimum, Node next){
            this.value = value;
            this.minimum = minimum;
            this.next = next;
        }
    }
    
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */