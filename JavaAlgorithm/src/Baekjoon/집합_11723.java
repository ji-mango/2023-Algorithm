package Baekjoon;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.util.Arrays;
import java.util.HashSet;
import java.util.StringTokenizer;

public class 집합_11723 {
    public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int M = Integer.parseInt(br.readLine());
        HashSet<Integer> array = new HashSet<Integer>();

        for(int i = 0; i < M; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            String command = st.nextToken();


            if(command.equals("all")) {
                array = new HashSet<>(Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20));
            }
            else if(command.equals("empty")) {
                array = new HashSet<Integer>();
            }

            else {
                Integer x = Integer.parseInt(st.nextToken());

                if (command.equals("add")) {
                    array.add(x);
                } else if (command.equals("remove")) {
                    array.remove(x);
                } else if (command.equals("check")) {
                    if (array.contains(x)) {
                        bw.write("1\n");
                    } else {
                        bw.write("0\n");
                    }
                } else if (command.equals("toggle")) {
                    if (array.contains(x)) {
                        array.remove(x);
                    } else {
                        array.add(x);
                    }
                }
            }
        }

        bw.flush();
    }
}
