#include <iostream>
#include <vector>
using namespace std;

int getMajorityElement(vector<int> arr)
{
    int n = arr.size();
    for (int i = 0; i < n; i++)
    {
        int frq = 0;
        for (int j = 0; j < n; j++)
        {
            if (arr[i] == arr[j])
                frq++;
        }
        if (frq > (n / 2))
            return arr[i];
    }
    return -1;
}

int main()
{
    int ans;
    vector<int> arr = {1, 5, 5, 1, 1, 1};
    ans = getMajorityElement(arr);
    cout << ans << endl;
}