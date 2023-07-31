//703. Kth Largest Element in a Stream

class KthLargest {
    PriorityQueue<Integer> minHeap = new PriorityQueue<>();
    int k;
    public KthLargest(int k, int[] nums) {
        
        this.k = k; //assign k value to global k
        for(int n: nums){
            minHeap.add(n); //add all value to the priority queue or we can call the class own add(int val) by using this.add(n);
        }
        
    }
    
    public int add(int val) {
        minHeap.add(val); //add "val" to the priority queue
        
        while(minHeap.size() > k){ //maintain Heap size as k so that the kth largest element (which is the minimum among all the elements in Heap of size k) will be at top of minHeap - this is the trick
            minHeap.remove();
        }
        
        return minHeap.peek(); //return top of minHeap
		
    }
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest obj = new KthLargest(k, nums);
 * int param_1 = obj.add(val);
 */