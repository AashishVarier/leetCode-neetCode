//74. Search a 2D Matrix

//matrix:M x N time:O(M + N) {at worst case, I will have to go through all row and do linear search in all column of that row ;space: O(1)
//This solutin is not binary search. Its staircase search O(n+m)
class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int i = 0, j = matrix[0].length - 1;
        
        while( i < matrix.length && j >= 0 ){
            if(target == matrix[i][j]){
                return true;
            }
            else if(target < matrix[i][j]){
                j --;
            }
            else{
                i ++;
            }
        }
        
        return false;
    }
}