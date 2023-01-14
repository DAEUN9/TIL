import java.util.Scanner;

public class B5_11021 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int T = scanner.nextInt();
        for (int i=1; i<T+1; i++) {
            int A = scanner.nextInt();
            int B = scanner.nextInt();
            System.out.println(String.format("Case #%s: %d", i, A+B));
        }

    }
}
