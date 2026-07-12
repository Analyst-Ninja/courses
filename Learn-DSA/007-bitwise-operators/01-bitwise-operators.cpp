#include <iostream>
using namespace std;

int main() {

    int a = 10, b = 9;

    // Bitwise AND operator
    cout << (a & b) << endl;

    // Bitwise OR operator
    cout << (a | b) << endl;

    // Bitwise XOR operator
    cout << (a ^ b) << endl;

    // Bitwise LeftShift operator --> Shifting the binary number with 1 bit
    cout << (a << 1) << endl; // this can shift by i number of places can be 1,2 ,3 etc
    cout << (a << 2) << endl; // this can shift by i number of places can be 1,2 ,3 etc

    // Bitwise RightShift operator --> Shifting the binary number with 1 bit
    cout << (a >> 1) << endl;
    cout << (a >> 2) << endl;
}

