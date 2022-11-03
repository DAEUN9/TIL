// https://school.programmers.co.kr/learn/courses/30/lessons/86051?language=java
class Solution {
    public int solution(int[] numbers) {
        int total = 0;
        int minus = 0;
        for (int i=0;i<10;i++) {
            total += i;
        }
        for (int num : numbers) {
            minus += num;
        }
        int answer = total - minus;
        return answer;
    }
}