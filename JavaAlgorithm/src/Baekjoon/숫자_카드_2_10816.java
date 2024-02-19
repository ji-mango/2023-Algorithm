package Baekjoon;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.*;

public class 숫자_카드_2_10816 {
    public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int N = Integer.parseInt(br.readLine());
        Map<Integer, Integer> cards = new HashMap<>();

        StringTokenizer st1 = new StringTokenizer(br.readLine());
        for(int i = 0; i < N; i++) {
            int num = Integer.parseInt(st1.nextToken());
            if (cards.get(num) == null) {
                cards.put(num, 1);
            }
            else {
                cards.put(num, cards.get(num) + 1);
            }
        }

        int M = Integer.parseInt(br.readLine());
        StringTokenizer st2 = new StringTokenizer(br.readLine());
        for (int i = 0; i < M; i ++) {
            int num = Integer.parseInt(st2.nextToken());

            if (cards.get(num) == null) {
                bw.write("0 ");
            }
            else {
                bw.write(cards.get(num).toString()+" ");
            }
        }

        bw.flush();
    }
}
