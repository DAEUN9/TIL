import java.util.Scanner;

public class B3_2525 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int A = sc.nextInt();
        int B = sc.nextInt();
        int C = sc.nextInt();

        A += C/60;
        B += C%60;
        A += B/60;
        B = B%60;

        if (A >= 24) {
            A = A%24;
        }
        System.out.print(A);
        System.out.print(" ");
        System.out.print(B);
    }
}
