// 브루트포스
// 영화감독 숌

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;

public class S5_1436 {
    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("input.txt"));
        BufferedReader sc = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(sc.readLine());
        int idx = 0;
        int num = 0;
        while (true) {
            num ++;
            if (String.valueOf(num).contains("666")) {
                idx ++;
            }
            if (idx>=N) {
                System.out.println(num);
                break;
            }
        }
    }

}
