import java.util.Scanner;

public class B5_25304 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int answer = sc.nextInt();
        int N = sc.nextInt();
        int total = 0;
        for(int i=0; i<N; i++) {
            total += sc.nextInt()*sc.nextInt();
        }
        if (total == answer) {
            System.out.println("Yes");
        }
        else {
            System.out.println("No");
        }
    }
}
