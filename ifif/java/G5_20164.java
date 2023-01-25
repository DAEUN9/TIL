// 홀수홀릭호석
// 구현

import java.io.*;

public class G5_20164 {
    static int minCnt = (int) 1e9;
    static int maxCnt = 0;

    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("input.txt"));
        BufferedReader sc = new BufferedReader(new InputStreamReader(System.in));
        String num = sc.readLine();
        solution(num, 0);
        System.out.print(minCnt+countOdd(num));
        System.out.print(" ");
        System.out.println(maxCnt+countOdd(num));
    }

    private static void solution(String num, int cnt) {
        if (num.length() == 1) {
            minCnt = Math.min(cnt, minCnt);
            maxCnt = Math.max(cnt, maxCnt);
            return;
        } else if (num.length() == 2) {
            int intNum = Character.getNumericValue(num.charAt(0)) + Character.getNumericValue(num.charAt(1));
            num = String.valueOf(intNum);
            cnt += countOdd(num);
            solution(num, cnt);
        }
        else {
            for (int i=1; i<num.length()-1; i++) {
                for (int j=i+1; j<num.length(); j++) {
                    String a = num.substring(0, i);
                    String b = num.substring(i, j);
                    String c = num.substring(j);
                    int intAbc = Integer.parseInt(a) + Integer.parseInt(b) + Integer.parseInt(c);
                    int tmp = countOdd(String.valueOf(intAbc));
                    solution(String.valueOf(intAbc), cnt+tmp);
                }
            }
        }
    }

    public static int countOdd(String number) {
        int cnt = 0;
        int n = Integer.parseInt(number);
        while (n>=1) {
            if ((n%10)%2 == 1) {
                cnt += 1;
            }
            n /= 10;
        }
        return cnt;
    }
}
