import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class B2_21918 {
    public static void main(String[] args) throws FileNotFoundException {
        System.setIn(new FileInputStream("input.txt"));
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        int[] lightArray = new int[N];
        for(int i=0; i<N; i++) {
            lightArray[i] = sc.nextInt();
        }
        for(int j=0; j<M; j++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            int c = sc.nextInt();
            lightArray = solution(lightArray, a, b, c);
        }
        for (int light : lightArray) {
            System.out.print(light);
            System.out.print(" ");
        }
    }

    public static int[] solution(int[] lightArray, int a, int b, int c) {
        if (a == 1){
            lightArray[b-1] = c;
            return lightArray;
        }
        if (a == 2){
            for(int i=b-1; i<c; i++) {
                lightArray[i] = (lightArray[i]+1)%2;
            }
            return lightArray;
        }
        if (a == 3){
            for(int i=b-1; i<c; i++) {
                lightArray[i] = 0;
            }
            return lightArray;
        }
        for(int i=b-1; i<c; i++) {
            lightArray[i] = 1;
        }
        return lightArray;
    }
}
