#include <iostream>
using namespace std;

int main() {
    int n = 10;
    int i = 1;

    // While Loop
    while (i <= n) {

        cout << i << " ";
        i++;

    }
    cout << endl << "while loop o/p" << endl;

    // For Loop
    for(int i = 1; i <= n; i++ ){
        cout << i << " ";
    }
    cout << endl << "for loop o/p" << endl;
    return 0;
}