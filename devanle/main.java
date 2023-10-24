package devanle;

import java.lang.reflect.Array;

public class main {
    // main class. doing nothing actually.
    public static void main(String[] args) {
        String[] rr = splitString("hsai,sjida00;sdjada,dau uand0;; ajnsa; dnaj]sj and:id a");
//        for(String s: rr)
//            System.out.println(s);
        int[] jj = {23, 32, 121, 32, 33, 2, 2, 2};
        Object obj  = jj;
        if(obj.getClass().isArray()){
            System.out.println("array");
        }
    }
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int hold = 0;
        for(int i = 0; i< m; i++){
            if(nums1[i] == 0 && i != 0)
                hold = 0;
        }
    }
    //writing spliting string
    public static String[] splitString(String arr){
        String[] arr1 = arr.split("[^a-zA-Z0-9]+");

        return arr1;
    }
}

