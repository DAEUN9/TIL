import java.io.*;

public class S4_1018 {
    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("input.txt"));
        BufferedReader sc = new BufferedReader(new InputStreamReader(System.in));
        String[] in = sc.readLine().split(" ");
        int N = Integer.parseInt(in[0]);
        int M = Integer.parseInt(in[1]);
        String[] arr = new String[N];
        for (int i=0; i<N; i++) {
            arr[i] = sc.readLine();
        }
        int minNum1 = (int) 1e9;
        int minNum2 = (int) 1e9;
        String[] WB = new String[] {"BWBWBWBW", "WBWBWBWB"};
        int idx = 1;
        for (int j=0; j<M-8+1; j++) {
            for (int i=0; i<N-8+1; i++) {
                int num1 = 0;
                int num2 = 0;
                for (int k=i; k<i+8; k++) {
                    String temp = arr[k].substring(j, j+8);
                    num1 += count(WB[(idx+1)%2], temp);
                    num2 += count(WB[(idx%2)], temp);
                    idx++;
                }
                minNum1 = Math.min(num1, minNum1);
                minNum2 = Math.min(num2, minNum2);
            }
        }
        System.out.println(Math.min(minNum1, minNum2));
    }

    private static int count(String a, String b) {
        int cnt = 0;
        for (int i=0; i<8; i++) {
            if (a.charAt(i) != b.charAt(i)) {
                cnt++;
            }
        }
        return cnt;
    }
}
