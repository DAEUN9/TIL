import java.util.Arrays;
import java.util.Collections;
import java.util.List;

class Solution {
    public int[] solution(int[] num_list) {
        List<Integer> list = Arrays.asList(num_list);
 
        Collections.reverse(list);
 
        int[] answer = list.toArray(list);
        return answer;
    }
}