class Solution {
    public int[] solution(int[] numbers, int num1, int num2) {
        int[] answer = new int[num2 - num1 + 1];

        int idx = -1;
        for (int i=num1; i<num2+1; i++) {
            idx += 1;
            answer[idx] = numbers[i];
        }
        return answer;
    }
}