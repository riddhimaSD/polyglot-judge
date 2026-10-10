import java.io.*;
import java.util.*;

public class Main {
    static int[] tmp;
    static long sort(int[] a, int lo, int hi) {
        if (hi - lo <= 1) return 0;
        int m = (lo + hi) >>> 1;
        long c = sort(a, lo, m) + sort(a, m, hi);
        int i = lo, j = m, k = lo;
        while (i < m && j < hi) {
            if (a[i] <= a[j]) tmp[k++] = a[i++];
            else { tmp[k++] = a[j++]; c += m - i; }
        }
        while (i < m) tmp[k++] = a[i++];
        while (j < hi) tmp[k++] = a[j++];
        for (int p = lo; p < hi; p++) a[p] = tmp[p];
        return c;
    }
    static String solve(String line) {
        StringTokenizer st = new StringTokenizer(line);
        int n = Integer.parseInt(st.nextToken());
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = Integer.parseInt(st.nextToken());
        tmp = new int[n];
        return String.valueOf(sort(a, 0, n));
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in), 1 << 16);
        int t = Integer.parseInt(br.readLine().trim());
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < t; i++) sb.append(solve(br.readLine())).append('\n');
        System.out.print(sb);
    }
}
