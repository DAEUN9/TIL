import java.util.Scanner;

public class B3_2884 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int hour = sc.nextInt();
        int minute = sc.nextInt();

        if (minute >= 45) {
            System.out.print(hour);
            System.out.print(" ");
            System.out.println(minute - 45);
        } else if (hour == 0) {
            System.out.print(23);
            System.out.print(" ");
            System.out.println(60 - (45 - minute));
        } else {
            System.out.print(hour -1);
            System.out.print(" ");
            System.out.println(60 - (45 - minute));
        }
    }
}
