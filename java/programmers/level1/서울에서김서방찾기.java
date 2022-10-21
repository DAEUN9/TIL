// https://school.programmers.co.kr/learn/courses/30/lessons/12919

class Solution {
    public String solution(String[] seoul) {
        String answer1 = "김서방은 ";
        String answer2 = "에 있다";
        int i = 0;
        for(String s : seoul) {
            if(s.equals("Kim")) {
                break;
            }
            i++;
        }
        String answer = "";
        answer += answer1;
        answer += i;
        answer += answer2;
        return answer;
    }
}