import java.util.*;

class Solution {
    public List<String> solution(String[] strArr) {
        List<String> answer = new ArrayList<>();
        int len = strArr.length;
        for (int i=0; i<len; i++) {
            if (i %2 == 0) {
                answer.add(strArr[i].toLowerCase());

            } else {
                answer.add(strArr[i].toUpperCase());
            }
        }
        return answer;
    }
}