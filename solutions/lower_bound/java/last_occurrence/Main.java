import java.io.*;
import java.util.*;

public class Main {
    static String solve(String line) {
        StringTokenizer st = new StringTokenizer(line);
        int n = Integer.parseInt(st.nextToken());
        int t = Integer.parseInt(st.nextToken());
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = Integer.parseInt(st.nextToken());
        int lo = 0, hi = n;
        while (lo < hi) {
            int mid = (lo + hi) >>> 1;
            if (a[mid] <= t) lo = mid + 1; else hi = mid;
        }
        return Integer.toString(lo > 0 && a[lo - 1] == t ? lo - 1 : lo);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in), 1 << 16);
        int t = Integer.parseInt(br.readLine().trim());
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < t; i++) sb.append(solve(br.readLine())).append('\n');
        System.out.print(sb);
    }
}
