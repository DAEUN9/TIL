// 랜선 자르기
// 매개변수 탐색, 이분탐색
// 주의!! N은 1이상 1,000,000이하 -> long타입

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;

public class S2_1654 {
    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("input.txt"));
        BufferedReader sc = new BufferedReader(new InputStreamReader(System.in));
        String[] in = sc.readLine().split(" ");
        int K = Integer.parseInt(in[0]);
        int N = Integer.parseInt(in[1]);
        long start = 1;
        long end = 0;
        long[] cableArr = new long[K];
        for (int i=0; i<K; i++){
            int cable = Integer.parseInt(sc.readLine());
            cableArr[i] = cable;
            end = Math.max(cable, end);
        }
        long middle = 0;
        while(start<=end) {
            middle = (start+end)/2;
            int cnt = 0;
            for (int i=0; i<K; i++){
                cnt += cableArr[i]/middle;
            }
            if (cnt >= N) {
                start = middle + 1;
            } else {
                end = middle -1;
            }
        }
        System.out.println(end);
    }
}
