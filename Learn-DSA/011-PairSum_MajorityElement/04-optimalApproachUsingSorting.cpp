#include <iostream>
#include <vector>
using namespace std;

int getMajorityElement(vector<int> &nums)
{
    int freq = 0;
    int currNum;
    int n = nums.size();

    // sort
    sort(nums.begin(), nums.end());

    // get the majority element
    for (int val : nums)
    {
        if (currNum != val)
        {
            currNum = val;
            freq = 0;
        }
        freq++;
        if (freq > n / 2)
            return currNum;
    }
    return -1;
}

int main()
{
    int ans;
    vector<int> nums = {1, 2, 2, 4, 2};
    ans = getMajorityElement(nums);
    cout << ans << endl;
}