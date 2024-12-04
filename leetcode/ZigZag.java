// platform: leetcode - https://leetcode.com/problems/zigzag-conversion/
// programming language: Java
// status: Accepted

// author: Gabriel Soares
// https://www.linkedin.com/in/gabrielsoarespebr/
// https://github.com/gabrielsoarespebr

import java.util.Arrays;

class Solution {
    public String convert(String textStart, int lineAmount) {
        if (lineAmount == 1) return textStart;

        int textLength = textStart.length();

        int id = 0;
        int idModifier = 1;

        String[] textPartList = new String[lineAmount];
        Arrays.fill(textPartList,"");

        String result = "";

        for (int i= 0; i < textLength; i++){
            textPartList[id] += textStart.charAt(i);

            if (id == 0) idModifier = 1;
            if (id == (lineAmount - 1)) idModifier = -1;

            id += idModifier;
        }

        for (int i = 0; i < lineAmount; i++){
            result += textPartList[i];
        }

        return result;
    }
}