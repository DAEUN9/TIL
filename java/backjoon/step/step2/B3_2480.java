import java.util.HashSet;
import java.util.Scanner;

public class B3_2480 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int A = sc.nextInt();
        int B = sc.nextInt();
        int C = sc.nextInt();

        HashSet set = new HashSet();
        set.add(A);
        set.add(B);
        set.add(C);

        if (set.size() == 1) {
            System.out.println(10000+A*1000);
        }
        else if (set.size() == 2) {
            if (A == B || A == C) {
                System.out.println(1000+A*100);
            }
            else {
                System.out.println(1000+B*100);
            }
        }
        else {
            System.out.println(calculateMax(A, B, C)*100);
        }
    }

    private static int calculateMax(int A, int B, int C) {
        if (A >= B && A >= C) {
            return A;
        }
        if (B >= C) {
            return B;
        }
        return C;
    }
}
