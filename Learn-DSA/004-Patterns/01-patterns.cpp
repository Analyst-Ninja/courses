#include <iostream>
using namespace std;

int main() {
    // Butterfly Pattern
    int n = 4;
    for (int i=0; i<n; i++) {
        for(int j=0; j<=i; j++) {
            cout << "*";
        }

        for (int j=0; j<2*n-2*i-2; j++) {
            if (i!=n-1) {
                cout << " ";
            }
        }

        for(int j=0; j<=i; j++) {
            cout << "*";
        }

        cout << endl;
    }

    for (int i=0; i<n; i++){
        for (int j=n; j>i; j--) {
            cout << "*";
        }
        for (int j=0; j<2*i; j++) {
                if (i!=0) {
                    cout << " ";
                }
            }
        for (int j=n; j>i; j--) {
            if (j!=0) {
                cout << "*";
            }
        }
        cout << endl;
    }

};
