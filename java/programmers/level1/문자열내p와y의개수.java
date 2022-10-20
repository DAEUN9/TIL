// https://school.programmers.co.kr/learn/courses/30/lessons/12916

class Solution {
    boolean solution(String s) {
        char[] chars = s.toCharArray();
        int p_cnt = 0;
        int y_cnt = 0;
        for(char a : chars) {
            a = Character.toLowerCase(a);
            if (a == 'p') {
                p_cnt += 1;
            } else if (a =='y') {
                y_cnt += 1;
            }
        }
        if ((p_cnt + y_cnt) == 0) {
            return true;
        } else if (p_cnt == y_cnt) {
            return true;
        };
        return false;

    }
}