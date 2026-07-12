#include <iostream>
#include <vector>
using namespace std;

int singleNumber(vector<int>& nums) {
    int ans = 0 ;
    for (int val : nums) {
        ans ^= val;
    }

    return ans;
}

int main() {
    vector <int> nums = {2,2,100};
    cout << singleNumber(nums) << endl;
}

// Bitwise Operations: XOR
// n^n = 0
// n^0 = n
