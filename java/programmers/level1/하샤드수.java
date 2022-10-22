# https://school.programmers.co.kr/learn/courses/30/lessons/12947?language=java

class Solution {
    public boolean solution(int x) {
        int y = x;
        int total = 0;
        while (y>=1) {
            total += y%10;
            y /= 10;
        }
        if (x%total==0) {
            return true;
        } else {
            return false;
        }
    }
}