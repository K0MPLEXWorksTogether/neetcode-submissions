class Solution {
    public int[] productExceptSelf(int[] nums) {
        int n = nums.length;
        int[] leftSum = new int[n];
        int[] rightSum = new int[n];

        int sum = 1;
        for(int i = 0; i < n; i++){
            sum *= nums[i];
            leftSum[i] = sum;
        }

        sum = 1;
        for(int i = n - 1; i >=0; i--){
            sum *= nums[i];
            rightSum[i] = sum;
        }

        int result[] = new int[n];
        for(int i = 0; i < n; i++){
            if(i == 0){
                result[i] = rightSum[i + 1];
            }
            else if(i == n - 1){
                result[i] = leftSum[i - 1];
            }
            else{
                result[i] = leftSum[i - 1] * rightSum[i + 1];
            }
        }

        return result;
    }
}  
