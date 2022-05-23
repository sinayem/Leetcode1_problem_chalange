class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int cs=0,ma=INT_MIN;
        //if(nums.size()==1)return nums[0];
        for(int i=0;i<nums.size();i++){
            cs+=nums[i];
            if(cs<nums[i])cs=nums[i];
            ma=max(ma,cs);
            
        }
        
        return ma;
    
    }
};
//https://leetcode.com/problems/maximum-subarray/
