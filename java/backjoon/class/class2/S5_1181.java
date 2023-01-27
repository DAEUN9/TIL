// 문자열, 정렬
// 단어 정렬

import java.io.BufferedReader;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class S5_1181 {
    public static void main(String[] args) throws IOException {
        System.setIn(new FileInputStream("input.txt"));
        BufferedReader sc = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(sc.readLine());
        Map<Integer, TreeSet<String>> wordMap = new HashMap<>();

        for (int t=0; t<T; t++) {
            String word = sc.readLine();
            TreeSet<String> wordSet = wordMap.getOrDefault(word.length(), new TreeSet<>());
            wordSet.add(word);
            wordMap.put(word.length(), wordSet);
        }

        List<Integer> keySet = new ArrayList<>(wordMap.keySet());
        Collections.sort(keySet);
        for (Integer key : keySet) {
            TreeSet<String> val = wordMap.get(key);
            Iterator iter = val.iterator();
            while(iter.hasNext()) {
                System.out.println(iter.next());
            }
        }
    }
}
