import java.io.*;
import java.util.Scanner;

public class G5_17609 {
    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("input.txt"));
        BufferedReader sc = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(sc.readLine());
        for(int t=0; t<T; t++){
            String S = sc.readLine();
            System.out.println(solution(S));
        }
    }

    private static int solution(String S) {
        if (isPal(S)) {
            return 0;
        }
        int cnt = 0;
        int start = 0;
        int end = S.length()-1;
        while (start<=end) {
            if (S.charAt(start) == S.charAt(end)) {
                start++;
                end--;
                continue;
            }

            cnt++;
            if (cnt>=2) {
                return 2;
            }
            if (S.charAt(start+1) != S.charAt(end)) {
                end--;
            } else if (S.charAt(start) != S.charAt(end-1)) {
                start++;
            }
            else {
              int temp_start = start+1;
              int temp_end = end;
              start++;
              while (temp_start<=temp_end) {
                  if (S.charAt(temp_start) == S.charAt(temp_end)) {
                      temp_start++;
                      temp_end--;
                      continue;
                  }
                  end--;
                  start--;
                  break;
              }

            }
        }
        return 1;
    }

    private static boolean isPal(String S) {
        for (int i=0; i<S.length(); i++) {
            if (S.charAt(i) != S.charAt(S.length()-i-1)) {
                return false;
            }
        }
        return true;
    }
}
