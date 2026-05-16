class Solution {
    public boolean hasDuplicate(int[] nums) {
        boolean answer = false;
        Arrays.sort(nums);

        for(int i = 1; i < nums.length; i++){
            if(nums[i] == nums[i - 1]){
                answer = true;
                return answer;
            }
        }
        return answer;
    }
}
