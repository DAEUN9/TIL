import java.util.Scanner;

public class B5_3003 {
    public static void main(String[] args) {
        int origin[] = {1, 1, 2, 2, 2, 8};

        Scanner sc = new Scanner(System.in);

        for(int i = 0; i < 6; i++) {
            System.out.print(origin[i] - sc.nextInt());
            System.out.print(" ");
        }
        sc.close();
    }
}
