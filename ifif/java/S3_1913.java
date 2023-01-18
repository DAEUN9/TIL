import java.io.*;
import java.util.Scanner;

public class S3_1913 {
    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("input.txt"));
        BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int N = Integer.parseInt(reader.readLine());
        int target = Integer.parseInt(reader.readLine());

        int num = N*N;
        int[][] arr = new int[N][N];
        int[][] direction = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};
        int idx = 0;
        int x = -1;
        int y = 0;
        int[] target_idx = {0, 0};
        while (num >=1) {
            int dx = x + direction[idx][0];
            int dy = y + direction[idx][1];
            if ((0<=dx && dx<N) && (0<=dy && dy<N) && arr[dx][dy]==0) {
                x = dx;
                y = dy;
                arr[x][y] = num;
                if (num == target) {
                    target_idx[0] = x+1;
                    target_idx[1] = y+1;
                }
                num--;
            }
            else {
                idx++;
                idx %= 4;
            }
        }
        for (int[] ar : arr) {
            for (int a : ar) {
                sb.append(a).append(" ");
            }
            sb.append("\n");
        }

        sb.append(target_idx[0]).append(" ").append(target_idx[1]);
        System.out.println(sb);
    }
}
