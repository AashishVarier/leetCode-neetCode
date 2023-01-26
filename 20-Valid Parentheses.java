//20. Valid Parentheses

class Solution {
    public boolean isValid(String s) {
        
        Stack<Character> stack = new Stack<>();
        Map<Character, Character> checkMap = new HashMap<>();
        
        checkMap.put(')' , '(');
        checkMap.put(']' , '[');
        checkMap.put('}' , '{');
        
        for(int i = 0; i < s.length(); i++){
            if(checkMap.containsKey(s.charAt(i))){
                if (!stack.isEmpty() && stack.peek() == checkMap.get(s.charAt(i))){
                        stack.pop();
                   }
            
                else {
                
                    return false;
                    }
                }
            else {
                stack.push(s.charAt(i));
            }    
        }
       return stack.isEmpty();
    }
}


///
class Solution {
    public boolean isValid(String s) {

        HashMap<Character, Character> dictMap = new HashMap<>();
        Stack<Character> parStack = new Stack();

        dictMap.put(')' , '(');
        dictMap.put(']' , '[');
        dictMap.put('}' , '{');

        for(Character c : s.toCharArray()){
            if(dictMap.containsValue(c)){
                parStack.push(c);
            }

           else if(!parStack.empty() && dictMap.containsKey(c) && dictMap.get(c).equals(parStack.peek())){
                parStack.pop();
            }

            else{
                return false;
            }

        }
        
        return parStack.empty();
    }
}