class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int m=0;
        int count=0;
        for(int i=0;i<nums.size();i++){
            if(nums[i]==1){
                count=count+1;
                m=max(m,count);
            }
            else{
                count=0;
            }
        }
        return m;
    }
};