import java.io.*;
import java.util.*;

public class Main {
    static String solve(String line) {
        StringTokenizer st = new StringTokenizer(line);
        int n = Integer.parseInt(st.nextToken());
        long best = 0, cur = 0;
        for (int i = 0; i < n; i++) {
            long x = Long.parseLong(st.nextToken());
            cur = Math.max(0, cur + x);
            best = Math.max(best, cur);
        }
        return Long.toString(best);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in), 1 << 16);
        int t = Integer.parseInt(br.readLine().trim());
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < t; i++) sb.append(solve(br.readLine())).append('\n');
        System.out.print(sb);
    }
}
