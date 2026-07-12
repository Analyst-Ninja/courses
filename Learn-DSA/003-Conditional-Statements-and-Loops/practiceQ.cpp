#include <iostream>
using namespace std;

int upperOrLowerWithASCII(char a) {

    if ((int)a < 97 && (int)a >= 65) {
        cout << "UpperCase with ASCII comparision method" << endl;
    } else if ((int)a >= 97 && (int)a < 123) {
        cout << "LowerCase with ASCII comparision method" << endl;
    } else {
        cout << "Not a Valid Character with ASCII comparision method" << endl;
    }

    return 0;
};

int upperOrLower(char a) {

    if (a >= 'A' && a <= 'Z' ) {
        cout << "UpperCase" << endl;
    } else if (a >= 'a' && a <= 'z' ) {
        cout << "LowerCase" << endl;
    } else {
        cout << "Not a Valid Character" << endl;
    }

    return 0;
};

int primeOrNot() {

    int n = 818937;

    for (int i = 2; i < n - 1; i++ ) {
        if (n % i == 0) {
            cout << "Non Prime" << endl;
            return 0;
        }
    }

    cout << "Prime" << endl;

    return 0;
};

int main(){

    // char ch;
    // cout << "Enter a charcter:- ";
    // cin >> ch;
    // upperOrLowerWithASCII(ch);
    // upperOrLower(ch);
    primeOrNot();

};

