import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int result = 0;
        char[][] arr = new char[8][8];
        for (int i = 0; i < 8; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String tmp = st.nextToken();
            for (int j = 0; j < 8; j++) {
                arr[i][j] = tmp.charAt(j);
            }
        }

        for (int i = 0; arr.length > i; i++) {
            for (int j = 0; j < arr[i].length; j++) {
                if(i % 2 == 0){
                    if(j % 2 == 0){
                        //하얀색
                        if(arr[i][j] == 'F'){
                            result++;
                        }
                    }
                }else{
                    if(j % 2 == 1){
                        // 하얀색
                        if(arr[i][j] == 'F'){
                            result++;
                        }
                    }
                }
            }
        }

        System.out.println(result);
    }
}