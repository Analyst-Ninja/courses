#include <iostream>
#include <vector>
using namespace std;

vector<int> pairSum(vector<int> nums, int targetSum)
{
    int arrSize = nums.size();
    int start = 0;
    int end = arrSize - 1;
    vector<int> ans;

    while (start < end)
    {
        int pairSum = nums[start] + nums[end];
        if (pairSum > targetSum)
        {
            end--;
        }
        else if (pairSum < targetSum)
        {
            start++;
        }
        else
        {
            ans.push_back(nums[start]);
            ans.push_back(nums[end]);
            return ans;
        }
    }

    return ans;
}

int main()
{
    vector<int> nums = {2, 3, 6, 11};
    int targetSum = 9;
    vector<int> ans;
    ans = pairSum(nums, targetSum);
    cout << ans[0] << ", " << ans[1] << endl;
    return 0;
}