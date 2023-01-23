import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class S5_6550 {
    public static void main(String[] args) {
        try {
            System.setIn(new FileInputStream("input.txt"));
        } catch (FileNotFoundException e) {
            throw new RuntimeException(e);
        }
        Scanner sc = new Scanner(System.in);
        while (true) {
            try {
                String words = sc.nextLine();
                System.out.println(solution(words));
            } catch (Exception e) {
                break;
            }

        }
    }

    private static String solution(String words) {
        String s = words.split(" ")[0];
        String t = words.split(" ")[1];
        int idx = 0;
        for (int i=0; i<t.length(); i++) {
            if(s.length()>idx && t.charAt(i) == s.charAt(idx)) {
                idx ++;
            }
            if (idx == s.length()) {
                return "Yes";
            }
        }
        return "No";

    }
}
