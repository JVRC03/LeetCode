class Solution {
public:
    int alternatingSum(vector<int>& nums) {

        int jvrc = 0;

        for(int i = 0; i < nums.size(); i++)
        {
            if(i%2 == 0)
            {
                jvrc += nums[i]; 
            }
            else{
                jvrc -= nums[i];
            }
        }
        
        return jvrc;
    }
};