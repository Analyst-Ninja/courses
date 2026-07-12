#include <iostream>
using namespace std;

int main() {
    int age = 25;
    char grade = 'A';
    float PI = 3.14f;
    bool isSafe = true;
    double price = 100.99;

    cout << age << endl;
    cout << isSafe<< endl;

    // bool retuen only in form of 0 or 1
    cout << "size of " << age << " is - " << sizeof(age) << endl;
    cout << "size of " << isSafe << " is - " << sizeof(isSafe) << endl;

    return 0;
}

// Data Types -- storage unit

// int - 4 bytes
// char - 1 byte
// float - 4 bytes
// bool - 1 byte
// double - 8 bytes