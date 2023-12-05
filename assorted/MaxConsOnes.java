class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int cnt = 0;        
        int count = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] == 1) {
                cnt++;
                if (cnt > count)
                    count = cnt;
            }
            else if (nums[i] == 0) {
                if (cnt > count)
                    count = cnt;
                cnt = 0;
            }
        }    
        
        return count;
    }
}