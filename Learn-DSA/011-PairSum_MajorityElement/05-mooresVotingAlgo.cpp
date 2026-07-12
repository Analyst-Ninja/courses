#include <iostream>
#include <vector>
using namespace std;

int getMajorityElement(vector<int> &nums)
{
    int freq = 0;
    int ans = 0;
    int n = nums.size();
    for (int i = 0; i < n; i++)
    {
        if (freq == 0)
        {
            ans = nums[i];
        }
        if (ans == nums[i])
            freq++;
        else
            freq--;
    }

    int count = 0;
    for (int val : nums)
    {
        if (val == ans)
            count++;
    }

    if (count > n / 2)
        return ans;
    else
        return -1;
}

int main()
{
    int ans;
    vector<int> nums = {1, 2, 2, 4, 2};
    ans = getMajorityElement(nums);
    cout << ans << endl;
}