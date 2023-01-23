import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class B1_10798 {
    public static void main(String[] args) throws FileNotFoundException {
        System.setIn(new FileInputStream("input.txt"));
        Scanner sc = new Scanner(System.in);
        String[] words = new String[5];
        int maxLen = 0;
        for (int i=0; i<5; i++) {
            words[i] = sc.nextLine();
            if (maxLen < words[i].length()) {
                maxLen = words[i].length();
            }
        }
        StringBuilder sb = new StringBuilder();
        for (int c=0; c<maxLen; c++) {
            for (int r=0; r<5; r++) {
                if (c<words[r].length()) {
                    sb.append(words[r].charAt(c));
                }
            }
        }
        System.out.println(sb);
    }
}
