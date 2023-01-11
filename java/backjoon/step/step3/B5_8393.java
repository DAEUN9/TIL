import java.util.Scanner;

public class B5_8393 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int total = 0;
        for(int i=0; i<n+1; i++) {
            total += i;
        }
        System.out.println(total);
    }
}
