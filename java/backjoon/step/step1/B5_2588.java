import java.util.Scanner;

public class B5_2588 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int A = sc.nextInt();
        int B = sc.nextInt();
        int result = A*B;
        while (B >= 1) {
            int C = B%10;
            B /= 10;
            System.out.println(A*C);
        }
        System.out.println(result);
    }
}
