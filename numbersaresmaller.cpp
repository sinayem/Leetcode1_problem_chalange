class Solution {
public:
    vector<int> smallerNumbersThanCurrent(vector<int>& nums) {
        map<int,int> m;
        int n=nums.size();
        vector<int>bb=nums;
        for(int i=0;i<n;i++){
            bb[i]=nums[i];
        }
        sort(bb.begin(),bb.end());
        for(int i=n-1;i>=0;i--){
            m[bb[i]]=i;
        }
        for(int i=0;i<n;i++){
            nums[i]=m[nums[i]];
        }
        return nums;
    }
};
//https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
