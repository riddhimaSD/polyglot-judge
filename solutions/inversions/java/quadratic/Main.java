import java.io.*;
import java.util.*;

public class Main {
    static String solve(String line) {
        StringTokenizer st = new StringTokenizer(line);
        int n = Integer.parseInt(st.nextToken());
        int[] a = new int[n];
        for (int i = 0; i < n; i++) a[i] = Integer.parseInt(st.nextToken());
        long c = 0;
        for (int i = 0; i < n; i++) for (int j = i + 1; j < n; j++) if (a[i] > a[j]) c++;
        return Long.toString(c);
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in), 1 << 16);
        int t = Integer.parseInt(br.readLine().trim());
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < t; i++) sb.append(solve(br.readLine())).append('\n');
        System.out.print(sb);
    }
}
