class Solution {
    public int maxArea(int[] heights) {
        int left = 0;
        int right = heights.length - 1;
        int maxWater = 0;
        int currWater = 0;
        while(left < right){
            int distance = right - left;
            if(heights[left] <= heights[right]){
                currWater = heights[left] * distance; 
                left++;
            }
            else{
                currWater = heights[right] * distance;
                right--;
            }

            if(currWater > maxWater) {
                maxWater = currWater;
            }
        }


        return maxWater;
    }
}
