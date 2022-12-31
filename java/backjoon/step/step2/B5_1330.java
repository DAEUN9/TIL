import java.util.Scanner;

public class B5_1330 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int A = sc.nextInt();
        int B = sc.nextInt();
        System.out.println(compare(A, B));
    }

    private static String compare(int A, int B) {
        if (A > B) {
            return ">";
        }
        if (A == B) {
            return "==";
        }
        return "<";
    }
}
