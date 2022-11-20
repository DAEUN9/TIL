class Solution {
    public int solution(int n) {
        int total = 0;
        for (int i=0; i<=n; i++) {
            if (i%2 == 0) {
                total += i;
            }
        }
        return total;
    }
}