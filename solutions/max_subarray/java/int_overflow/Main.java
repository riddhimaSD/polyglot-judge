import java.io.*;
import java.util.*;

public class Main {
    static String solve(String line) {
        StringTokenizer st = new StringTokenizer(line);
        int n = Integer.parseInt(st.nextToken());
        int best = Integer.parseInt(st.nextToken()), cur = best;
        for (int i = 1; i < n; i++) {
            int x = Integer.parseInt(st.nextToken());
            cur = Math.max(x, cur + x);
            best = Math.max(best, cur);
        }
        return Integer.toString(best);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in), 1 << 16);
        int t = Integer.parseInt(br.readLine().trim());
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < t; i++) sb.append(solve(br.readLine())).append('\n');
        System.out.print(sb);
    }
}
