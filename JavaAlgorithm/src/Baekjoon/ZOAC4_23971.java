package Baekjoon;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class ZOAC4_23971 {
        public static void main(String[] args) throws Exception {
            BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

            StringTokenizer st = new StringTokenizer(br.readLine());
            int H = Integer.parseInt(st.nextToken());
            int W = Integer.parseInt(st.nextToken());
            int N = Integer.parseInt(st.nextToken());
            int M = Integer.parseInt(st.nextToken());

            int column = W / (M+1);
            int row = H / (N+1);

            if (W % (M+1) != 0) {
                column += 1;
            }
            if (H % (N+1) != 0) {
                row += 1;
            }

            System.out.println(column*row);
        }
    }