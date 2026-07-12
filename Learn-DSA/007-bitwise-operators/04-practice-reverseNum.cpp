#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int N = 123;
    int revNum = 0;
    
    while (N > 0) {
        int rem;
        rem = N % 10;
        revNum = revNum * 10 + rem;
        N = N/10;
    }

    cout << "Reversed Number --> " << revNum << endl;

}