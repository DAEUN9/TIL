// 스택 수열
// 스택

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class S2_1874 {
    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("input.txt"));
        BufferedReader sc = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(sc.readLine());
        int[] arr = new int[N];
        for (int i=0; i<N; i++) {
            arr[i] = Integer.parseInt(sc.readLine());
        }
        solution(N, arr);
    }

    private static void solution(int N, int[] arr) {
        Stack<Integer> stack = new Stack<>();
        int idx = 0;
        List<String> answer = new ArrayList<>();
        for (int n=1; n<N+1; n++) {
            if (arr[idx] >= n) {
                stack.push(n);
                answer.add("+");
            }
            while (!stack.isEmpty() && stack.peek() == arr[idx]) {
                stack.pop();
                answer.add("-");
                idx++;
            }
        }
        if (!stack.isEmpty() || idx<N-1) {
            System.out.println("NO");
            return;
        }
        for (String a: answer) {
            System.out.println(a);
        }
    }
}
