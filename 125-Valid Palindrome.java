//125. Valid Palindrome

// two pointer
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


// checking reverse string
class Solution {
    public boolean isPalindrome(String s) {
        
        String revString,toCheck;
        
        toCheck = isAlpha(s);
        revString = new StringBuilder(toCheck).reverse().toString();

        if(revString.equals(toCheck)){
        return true;
        }
        else{
            return false;
        }
    }

    public String isAlpha(String str){
        char c;
        StringBuilder sb = new StringBuilder();

        for(int i =0; i< str.length(); i++)
        {   
            c = str.charAt(i);
            if( Character.isLetterOrDigit(c)){
                sb.append(c);
            }
            
        }
       return sb.toString().toLowerCase();

    }
}
