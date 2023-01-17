import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class B2_2920 {
    public static void main(String[] args) throws FileNotFoundException {
        System.setIn(new FileInputStream("input.txt"));
        Scanner sc = new Scanner(System.in);
        int[] pitchs = new int[8];
        pitchs[0] = sc.nextInt();
        if (pitchs[0]==1 || pitchs[0]==8) {
            System.out.println(solution(pitchs, sc));
        }
        else {
            System.out.println("mixed");
        }

    }

    public static String solution(int[] pitchs, Scanner sc) {
        int flag;
        if(pitchs[0] == 1){
            flag = 1;
        }
        else {
            flag = -1;
        }
        for (int i=1; i<8; i++) {
            pitchs[i] = sc.nextInt();
            if (pitchs[i-1]+flag != pitchs[i]) {
                return "mixed";
            }
        }
        if (flag==1) {
            return "ascending";
        }
        return "descending";
    }
}
