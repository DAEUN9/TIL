import java.util.Arrays;

class Solution {
    public double solution(int[] numbers) {
        double sum = Arrays.stream(numbers).sum();
        return sum/numbers.length;
    }
}