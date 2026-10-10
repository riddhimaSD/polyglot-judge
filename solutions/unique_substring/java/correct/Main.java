import java.io.*;
import java.util.*;

public class Main {
    static String solve(String line) {
        String s = line.trim();
        int[] last = new int[128];
        Arrays.fill(last, -1);
        int left = 0, best = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (last[c] >= 0) left = Math.max(left, last[c] + 1);
            last[c] = i;
            best = Math.max(best, i - left + 1);
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
