class Solution {
    public boolean isValid(String s) {
        Stack<Character> stk = new Stack<>();

        for(char ch: s.toCharArray()){
            if(ch == '(' || ch == '{' || ch == '['){
                stk.push(ch);
            }
            else if(ch == ')'){
                if(stk.size() == 0){
                    return false;
                }
                char popped = stk.pop();
                if(popped != '('){
                    return false;
                }
            }
            else if(ch == '}'){
                if(stk.size() == 0){
                    return false;
                }
                char popped = stk.pop();
                if(popped != '{'){
                    return false;
                }
            }
            else if(ch == ']'){
                if(stk.size() == 0){
                    return false;
                }
                char popped = stk.pop();
                if(popped != '['){
                    return false;
                }
            }
        }

        if(stk.size() == 0){
            return true;
        } 
        else{
            return false;
        }
    }
}