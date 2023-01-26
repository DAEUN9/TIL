// 문자열 게임2
// 문자열, 슬라이딩 윈도우

import java.io.*;
import java.util.*;

public class G5_20437 {
    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("input.txt"));
        BufferedReader sc = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(sc.readLine());
        for (int t=0; t<T; t++) {
            String W = sc.readLine();
            int K = Integer.parseInt(sc.readLine());
            int[] answer = solution(W, K);
            for (int an : answer) {
                System.out.print(an);
                System.out.print(" ");
            }
            System.out.println();
        }
    }

    public static long countChar(String str, char ch) {
        return str.chars()
                .filter(c -> c == ch)
                .count();
    }
    private static int[] solution(String W, int K) {
        Map<Character, List<Integer>> map = new HashMap<>();
        for (int i=0; i<W.length(); i++) {
            if (countChar(W, W.charAt(i)) < K) {
                continue;
            }
            List<Integer> arrayList = map.getOrDefault(W.charAt(i), new ArrayList<>());
            arrayList.add(i);
            map.put(W.charAt(i), arrayList);
        }

        if (map.size() == 0) {
            return new int[]{-1};
        }
        int[] answer = new int[] {(int) 1e9, 0};
        for (List<Integer> val : map.values()) {
            for (int j=0; j<val.size()-K+1; j++) {
                int temp = val.get(j+K-1) - val.get(j) + 1;
                answer[0] = Math.min(answer[0], temp);
                answer[1] = Math.max(answer[1], temp);
            }
        }
        return answer;
    }
}
