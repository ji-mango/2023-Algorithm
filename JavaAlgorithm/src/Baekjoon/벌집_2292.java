package Baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class 벌집_2292 {
    public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        int count = 1;
        int present = 1;
        while(true) {
            if(N <= present) {
                System.out.println(count);
                break;
            }

            else {
                present = present + 6 * count;
                count += 1;
            }
        }
    }
}