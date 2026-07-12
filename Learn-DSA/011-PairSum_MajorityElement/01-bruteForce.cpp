#include <iostream>
#include <vector>
using namespace std;

int main()
{
    vector<int> nums = {2, 7, 11, 13};
    int sum;
    int arrSize = sizeof(nums) / sizeof(int);
    int targetSum = 20;

    for (int i = 0; i < arrSize; i++)
    {
        for (int j = i + 1; j < arrSize; j++)
        {
            if ((nums[i] + nums[j]) == targetSum)
            {
                cout << "(" << nums[i] << "," << nums[j] << ")" << endl;
            }
        }
    }
}