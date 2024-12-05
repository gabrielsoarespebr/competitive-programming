// platform: leetcode - https://leetcode.com/problems/move-pieces-to-obtain-a-string
// programming language: Java
// status: In progress

// author: Gabriel Soares
// https://www.linkedin.com/in/gabrielsoarespebr/
// https://github.com/gabrielsoarespebr

import java.util.List;
import java.util.ArrayList;

public class MovePiecesToObtainAString {
    public static void canChange(String start, String target) {
        int lAmount = 0;
        List<Integer> lStartIdList = new ArrayList<>();
        List<Integer> lTargetIdList = new ArrayList<>();

        int rAmount = 0;
        List<Integer> rStartIdList = new ArrayList<>();
        List<Integer> rTargetIdList = new ArrayList<>();

        List<Integer> emptyStartIdList = new ArrayList<>();

        for (int i = 0; i < start.length(); i++) {
            // L
            if (start.charAt(i) == 'L') {
                lAmount++;
                lStartIdList.add(i);
            }
            if (target.charAt(i) == 'L') {
                lTargetIdList.add(i);
            }

            // R
            if (start.charAt(i) == 'R') {
                rAmount++;
                rStartIdList.add(i);
            }
            if (target.charAt(i) == 'R') {
                rTargetIdList.add(i);
            }

            // EMPTY
            if (start.charAt(i) == '_') {
                emptyStartIdList.add(i);
            }
        }

        System.out.println("L: " + lAmount);
        System.out.println("L start id: " + lStartIdList);
        System.out.println("L start id: " + lTargetIdList);
        System.out.println();
        System.out.println("R: " + rAmount);
        System.out.println("R start id: " + rStartIdList);
        System.out.println("R target id: " + rTargetIdList);
        System.out.println();
        System.out.println("_ start id: " + emptyStartIdList);
    }

    public static void main(String[] args) {
        canChange("_L__R__R_", "L______RR");
    }
}