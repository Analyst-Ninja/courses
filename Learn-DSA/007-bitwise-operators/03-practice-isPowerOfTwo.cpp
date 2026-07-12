#include <iostream>
using namespace std;

int main() {
    int N = 32;
    int pow = 1;

    while (pow < N) {
        pow = pow << 1;
    }

    if (pow == N) {
        cout << N << " --> " << "is Power of 2" << endl;
    } else {
        cout << N << " --> " << "is not Power of 2" << endl;
    }
}