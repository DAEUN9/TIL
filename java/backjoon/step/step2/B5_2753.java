import java.util.Scanner;

public class B5_2753 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int year = sc.nextInt();
        System.out.println(solve(year));
    }
    private static int solve(int year) {
        if (year%4 > 0) {
            return 0;
        }
        if (year%100 > 0) {
            return 1;
        }
        if (year%400 > 0) {
            return 0;
        }
        return 1;
    }
}
