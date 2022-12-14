class Solution {
    public String solution(String my_string) {
        String answer = "";
        for (int i=0; i<my_string.length(); i++){
            answer = my_string.charAt(i) + answer;
        }
        return answer;
    }
}