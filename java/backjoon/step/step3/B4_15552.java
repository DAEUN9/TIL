import java.io.*;
import java.util.StringTokenizer;

public class B4_15552 {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bufferedWriter = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer stringTokenizer;
        String t = bufferedReader.readLine();
        int T = Integer.parseInt(t);
        for (int i=0; i<T; i++) {
            stringTokenizer = new StringTokenizer(bufferedReader.readLine());
            bufferedWriter.write(Integer.parseInt(stringTokenizer.nextToken()) + Integer.parseInt(stringTokenizer.nextToken()) +"\n" );
        }
        bufferedWriter.flush();
    }
}
