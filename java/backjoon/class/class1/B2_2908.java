import java.util.Scanner;

public class B2_2908 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String A = sc.next();
        String B = sc.next();
        for (int i=A.length()-1; i>-1; i--) {
            if (A.charAt(i) > B.charAt(i)) {
                StringBuffer sb = new StringBuffer(A);
                String reversedStr = sb.reverse().toString();
                System.out.println(reversedStr);
                break;
            }
            else if (A.charAt(i) < B.charAt(i)) {
                StringBuffer sb = new StringBuffer(B);
                String reversedStr = sb.reverse().toString();
                System.out.println(reversedStr);
                break;
            }
        }
    }
}
