package devanle;

public class MyPow {

    public static void main(String[] args) {
        System.out.println(myPow(3,3));

    }
    public static double myPow(double x, int n) {
        if(n == 0)
            return 1;
        if(n == 1)
            return x;
        x=x*x;
        return myPow(x, n-1);
    }
}
