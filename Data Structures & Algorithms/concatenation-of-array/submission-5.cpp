class Solution {
public:
    vector<int> getConcatenation(vector<int>& nums) {
        vector<int> ans=nums;
        int s=nums.size();
        for(int i:nums){
            ans.push_back(i);
        }
        return ans;
    }
};