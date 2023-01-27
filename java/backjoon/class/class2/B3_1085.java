import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;

public class B3_1085 {
    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("input.txt"));
        BufferedReader sc = new BufferedReader(new InputStreamReader(System.in));
        String[] in = sc.readLine().split(" ");
        int x = Integer.parseInt(in[0]);
        int y = Integer.parseInt(in[1]);
        int w = Integer.parseInt(in[2]);
        int h = Integer.parseInt(in[3]);
        int temp = Math.min(Math.abs(x-w), Math.abs(y-h));
        temp = Math.min(temp, x);
        temp = Math.min(temp, y);
        System.out.println(temp);
    }
}
