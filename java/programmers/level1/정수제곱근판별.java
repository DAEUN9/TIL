// https://school.programmers.co.kr/learn/courses/30/lessons/12934

class Solution {
    public long solution(long n) {
        long answer = 0;
        while (n/2>=answer) {
            answer+=1;
            if (answer*answer == n) {
                return (answer+1)*(answer+1);
            }
        }
        return -1;
    }
}