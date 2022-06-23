//125. Valid Palindrome

class Solution {
    public boolean isPalindrome(String s) {
        
        String strToCheck = s.toLowerCase();
        
        int i = 0 , j = s.length() - 1;
        
        if(s.isEmpty())
            return true;
        
        while( i <= j ) {
            if (!Character.isLetterOrDigit(strToCheck.charAt(i))){
                i ++ ;
				}
                else if ((!Character.isLetterOrDigit(strToCheck.charAt(j)))){
                    j --;
					}
                     else {
						if(strToCheck.charAt(i) != strToCheck.charAt(j)){
                             return false;
                         }
                                 i++;
                                 j--;
							}
        }
                                 
        return true;
        
    }
}