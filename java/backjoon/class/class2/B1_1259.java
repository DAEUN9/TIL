import java.io.*;
import java.util.Objects;

public class B1_1259 {
    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("input.txt"));
        BufferedReader sc = new BufferedReader(new InputStreamReader(System.in));
        while (true) {
            String S = sc.readLine();
            if (Objects.equals(S, "0")) {
                break;
            }
            System.out.println(solution(S));
        }
    }

    private static String solution(String S) {
        int start = 0;
        int end = S.length()-1;
        while (start<=end) {
            if (S.charAt(start) == S.charAt(end)) {
                start++;
                end--;
                continue;
            }
            return "no";
        }
        return "yes";
    }
}
