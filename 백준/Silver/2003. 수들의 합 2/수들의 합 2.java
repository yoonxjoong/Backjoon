import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[] a = new int[n];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            a[i] = Integer.parseInt(st.nextToken());
        }

        int start_index = 0;
        int end_index = 0;

        int count = 0;
        int sum = 0;

        while (end_index <= n) {
            if (sum < m) {
                if (end_index == n) // 만약 end_index가 n에 도달하면 루프 종료
                    break;
                sum += a[end_index];
                end_index++;
            } else if (sum == m) {
                count++;
                sum -= a[start_index];
                start_index++;
            } else {
                sum -= a[start_index];
                start_index++;
            }
        }
        System.out.println(count);
    }
}