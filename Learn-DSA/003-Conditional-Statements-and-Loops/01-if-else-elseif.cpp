#include <iostream>
using namespace std;

int main() {
    int num;

    cout << "Enter a Number:- ";
    cin >> num;

    if (num >= 0) {
        cout << "Positive Number" << endl;
    } else {
        cout << "Negative Number" << endl;
    }

    return 0;
}