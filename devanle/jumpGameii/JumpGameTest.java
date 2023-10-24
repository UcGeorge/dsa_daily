package devanle.jumpGameii;

import org.junit.*;

import static org.junit.Assert.assertEquals;

public class JumpGameTest {
    private static Solution solution;
    @Test
    public void testJump(){
        int[] nums = {2, 3, 1, 1, 4};
        int expectedResult = 2; //expected result from the method

        int result = solution.jump(nums);
        assertEquals(expectedResult, result);
    }
}
