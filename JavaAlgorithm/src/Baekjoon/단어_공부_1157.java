package Baekjoon;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;


public class 단어_공부_1157 {
    public static void main(String args[]) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String word = br.readLine();
        word = word.toUpperCase();

        Map<Character, Integer> word_dict = new HashMap();
        for(int i = 0; i < word.length(); i++) {
            if(word_dict.get(word.charAt(i)) == null) {
                word_dict.put(word.charAt(i), 1);
            }
            else {
                word_dict.put(word.charAt(i), word_dict.get(word.charAt(i)) + 1);
            }
        }

        int max_length = 0;
        char answer = '?';
        for(Character c : word_dict.keySet()) {
            if (max_length < word_dict.get(c)) {
                max_length = word_dict.get(c);
                answer = c;
            }
            else if ((max_length == word_dict.get(c)) ) {
                answer = '?';
            }
        }

        System.out.println(answer);
    }
}
