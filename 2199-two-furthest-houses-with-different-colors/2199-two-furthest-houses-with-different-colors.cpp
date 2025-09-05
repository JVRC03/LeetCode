class Solution {
public:
    int maxDistance(vector<int>& arr) {
        int jvrc = 0;

        for(int i = 0; i < arr.size(); i++)
        {
            for(int j = i+1; j < arr.size(); j++)
            {
                if(arr[i] != arr[j])
                {
                    if(abs(i-j) > jvrc)
                    {
                        jvrc = abs(i-j);
                    }
                }
            }
        }

        return jvrc; 

    }
};