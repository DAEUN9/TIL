// 문자열
// 싸이버개강총회

import java.io.*;
import java.util.*;

public class S2_19583 {
    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("input.txt"));
        BufferedReader sc = new BufferedReader(new InputStreamReader(System.in));
        String[] line = sc.readLine().split(" ");
        int S = convertNumber(line[0]);
        int E = convertNumber(line[1]);
        int Q = convertNumber(line[2]);

        Map<String, Integer> nameMap = new HashMap<>();
        int cnt = 0;
        String[] chat;
        while (true) {
            try {
                chat = sc.readLine().split(" ");
            }
            catch(Exception e) {
                break;
            }
            int curr = convertNumber(chat[0]);
            if (curr <= S) {
                nameMap.put(chat[1], 0);
            } else if (E <= curr && curr <= Q) {
                if (nameMap.getOrDefault(chat[1], -1) == 0) {
                    nameMap.replace(chat[1], 1);
                }
            }
        }
        for (int i : nameMap.values()) {
            if (i==1) {
                cnt += 1;
            }

        }
        System.out.println(cnt);
    }
    private static int convertNumber(String time) {
        String[] timeArray = time.split(":");
        return Integer.parseInt(timeArray[0])*60 + Integer.parseInt(timeArray[1]);
    }
}
