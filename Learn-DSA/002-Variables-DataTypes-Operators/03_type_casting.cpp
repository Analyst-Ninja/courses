#include <iostream>
using namespace std;

int main() {
    float price = 100.99;
    char grade = 'A'; // 65 in ASCII

    // Type Conversion 
    int newGrade = grade;
    cout << "Old Grade -> " << grade << "newGrade -> " << newGrade << endl;

    // Type Casting
    int newPrice = (int)price;
    cout << "Old Price -> " << price << "newPrice -> " << newPrice << endl;

    return 0;

}