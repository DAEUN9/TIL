// https://school.programmers.co.kr/learn/courses/30/lessons/12910?language=java

import java.util.*;

class Solution {
    public int[] solution(int[] arr, int divisor) {
        int[] answer = {};
        ArrayList<Integer> answer2 = new ArrayList<Integer>();
        for(int a: arr) {
            if (a%divisor==0) {
                answer2.add(a);
            }
                
        }
        if (answer2.isEmpty()) {
            answer2.add(-1);
        }
        answer = new int[answer2.size()];
        for(int i=0; i<answer2.size(); i++) {
              answer[i] = answer2.get(i);
          }
          
        Arrays.sort(answer);
        return answer;
    }
}