import java.io.*;
import java.util.StringTokenizer;

public class S1_16926 {
    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("input.txt"));
        BufferedReader sc = new BufferedReader(new InputStreamReader(System.in));
        String[] NMR = sc.readLine().split(" ");
        int N = Integer.parseInt(NMR[0]);
        int M = Integer.parseInt(NMR[1]);
        int R = Integer.parseInt(NMR[2]);

        int[][] arr = new int[N][M];
        for (int n=0; n<N; n++) {
            StringTokenizer st = new StringTokenizer(sc.readLine());
            for (int m=0; m<M; m++) {
                arr[n][m] = Integer.parseInt(st.nextToken());
            }
        }

        for (int i=0; i<R; i++) {
            for (int j=0; j<Math.min(N, M)/2; j++) {
                int x = j;
                int y = j;
                int temp = arr[x][y];
                int pre = 0;

                for (int a=j+1; a<N-j; a++) {
                    x = a;
                    pre = arr[x][y];
                    arr[x][y] = temp;
                    temp = pre;
                }

                for (int a=j+1; a<M-j; a++) {
                    y = a;
                    pre = arr[x][y];
                    arr[x][y] = temp;
                    temp = pre;
                }

                for (int a=N-j-2; a>j-1; a--) {
                    x = a;
                    pre = arr[x][y];
                    arr[x][y] = temp;
                    temp = pre;
                }

                for (int a=M-j-2; a>j-1; a--) {
                    y = a;
                    pre = arr[x][y];
                    arr[x][y] = temp;
                    temp = pre;
                }
            }
        }

        for (int[] ar : arr) {
            for (int a : ar) {
                System.out.print(a);
                System.out.print(" ");
            }
            System.out.println();
        }
    }
}
