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

        st = new StringTokenizer(br.readLine());
        char[] chars = st.nextToken().toCharArray();

        st = new StringTokenizer(br.readLine());
        int[] cnt = new int[4];

        for (int i = 0; i < cnt.length; i++) {
            cnt[i] = Integer.parseInt(st.nextToken());
        }

        int start = 0;
        int end = m;
        int result = 0;

        // Precompute counts of each nucleotide in the whole sequence
        int[] nucleotideCount = new int[4];
        for (int i = 0; i < m; i++) {
            if (chars[i] == 'A') nucleotideCount[0]++;
            else if (chars[i] == 'C') nucleotideCount[1]++;
            else if (chars[i] == 'G') nucleotideCount[2]++;
            else if (chars[i] == 'T') nucleotideCount[3]++;
        }

        while (end <= n) {
            int a = cnt[0];
            int c = cnt[1];
            int g = cnt[2];
            int t = cnt[3];

            // Check if the current substring satisfies the conditions
            if (nucleotideCount[0] >= a && nucleotideCount[1] >= c &&
                    nucleotideCount[2] >= g && nucleotideCount[3] >= t) {
                result++;
            }

            // Update nucleotide counts for the next substring
            if (end < n) {
                if (chars[start] == 'A') nucleotideCount[0]--;
                else if (chars[start] == 'C') nucleotideCount[1]--;
                else if (chars[start] == 'G') nucleotideCount[2]--;
                else if (chars[start] == 'T') nucleotideCount[3]--;

                if (chars[end] == 'A') nucleotideCount[0]++;
                else if (chars[end] == 'C') nucleotideCount[1]++;
                else if (chars[end] == 'G') nucleotideCount[2]++;
                else if (chars[end] == 'T') nucleotideCount[3]++;
            }

            start++;
            end++;
        }

        System.out.println(result);

    }
}


