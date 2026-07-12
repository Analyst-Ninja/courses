#include <iostream>
#include <vector>
using namespace std;

int linearSearch(vector<int> nums, int valueTosearch)
{
    int vecSize = sizeof(nums) / sizeof(int);
    for (int i = 0; i < vecSize; i++)
    {
        if (valueTosearch == nums[i])
            return i;
    }
    return -1;
}

void reverseVector(vector<int> &nums)
{
    int vecSize = sizeof(nums) / sizeof(int);
    int start = 0;
    int end = vecSize - 1;

    while (start < end)
    {
        swap(nums[start], nums[end]);
        start++;
        end--;
    }
}

int main()
{
    vector<int> nums = {1, 2, 3, 4, 5, 6};
    int valToSearch = 5;

    cout << linearSearch(nums, valToSearch) << endl;

    reverseVector(nums);

    for (int val : nums)
    {
        cout << val << " ";
    }
    // for (int val : ) {
    //     cout << val << " ";
    // }
    cout << endl;
}