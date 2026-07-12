#include <iostream>
using namespace std;

// decimal to binary number conversion
int decimalToBinary(int N) {
    int pow = 1, rem, ans = 0;

    while (N > 0) {
        rem = N % 2;
        N = N / 2;
        ans += rem * pow;
        pow *= 10;
    }
    return ans;
}

// binary to decimal number conversion
int binaryToDecimal(int N) {
    int pow = 1, rem, ans = 0;

    while (N > 0) {
        rem = N % 10;
        N = N / 10;
        ans += rem * pow;
        pow *= 2;
    }
    return ans;
}


int main() {

    int N = 10;
    
    for (int i = 1; i <= N; i++) {
        int binaryNum;
        binaryNum = decimalToBinary(i);
        cout << i << " ==> " << binaryNum << endl; 
    }

    int binaryNo = 1010; 
    cout << binaryNo << " ===> " << binaryToDecimal(binaryNo) << endl;

}