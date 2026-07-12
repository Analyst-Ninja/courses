#include <iostream>
#include <vector>
#include <climits>
using namespace std;

int main()
{
    vector<int> vec = {1, -3, 6, 7, 8, -10};
    int vecSize = vec.size();
    int currSum = 0;
    int maxSum = INT_MIN;

    for (int i = 0; i < vecSize; i++)
    {
        currSum = 0;
        for (int j = i; j < vecSize; j++)
        {
            currSum += vec[j];
            maxSum = max(currSum, maxSum);
        }
        cout << maxSum << " ";
    }
    cout << "\nMax Sub Array Sum: " << maxSum << endl;
}