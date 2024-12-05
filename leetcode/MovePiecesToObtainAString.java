// platform: leetcode - https://leetcode.com/problems/move-pieces-to-obtain-a-string
// programming language: Java
// status: Time Limit Exceeded

// author: Gabriel Soares
// https://www.linkedin.com/in/gabrielsoarespebr/
// https://github.com/gabrielsoarespebr

import java.util.List;
import java.util.ArrayList;

public class MovePiecesToObtainAString {

    public static boolean canChange(String start, String target) {
        int lAmount = 0;
        int lAmountEnd = 0;
        List<Integer> lStartIdList = new ArrayList<>();
        List<Integer> lTargetIdList = new ArrayList<>();

        int rAmount = 0;
        int rAmountEnd = 0;
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
                lAmountEnd++;
                lTargetIdList.add(i);
            }

            // R
            if (start.charAt(i) == 'R') {
                rAmount++;
                rStartIdList.add(i);
            }
            if (target.charAt(i) == 'R') {
                rAmountEnd++;
                rTargetIdList.add(i);
            }

            // EMPTY
            if (start.charAt(i) == '_') {
                emptyStartIdList.add(i);
            }
        }

        if (lAmount != lAmountEnd) return false;
        if (rAmount != rAmountEnd) return false;

        // LEFT
        for(int i=0;i<lAmount;i++){
            int moveAmount = lStartIdList.get(i) - lTargetIdList.get(i);

            // negative moveAmount means wrong moves
            if (moveAmount < 0) return false;

            for(int j = 0; j < moveAmount; j++){
                int numberPrevious = lStartIdList.get(i) - 1;

                int indexPrevious = emptyStartIdList.indexOf(numberPrevious);

                // check if left position is empty
                if (indexPrevious != -1){
                    emptyStartIdList.set(indexPrevious, lStartIdList.get(i));
                    lStartIdList.set(i,numberPrevious);
                } else{
                    return false;
                }
            }
        }

        // RIGHT
        for(int i=rAmount-1;i>=0;i--){
            int moveAmount = rTargetIdList.get(i) - rStartIdList.get(i);

            // negative moveAmount means wrong moves
            if (moveAmount < 0) return false;

            for(int j = 0; j < moveAmount; j++){
                int numberNext = rStartIdList.get(i) + 1;

                int indexNext = emptyStartIdList.indexOf(numberNext);

                // check if right position is empty
                if (indexNext != -1){
                    emptyStartIdList.set(indexNext, rStartIdList.get(i));
                    rStartIdList.set(i,numberNext);
                } else{
                    return false;
                }
            }
        }
        
        return true;
    }

    public static void main(String[] args) {
        
        boolean result = canChange("_R", "R_");
        System.out.println(result);
    }
}