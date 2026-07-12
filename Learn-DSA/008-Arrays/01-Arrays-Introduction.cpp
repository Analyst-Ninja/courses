#include <iostream>
using namespace std;

int main()
{
    int size = 5;
    int marks[size];

    cout << "Enter the marks" << endl;
    for (int i = 0; i < size; i++)
    {
        cin >> marks[i];
    }

    cout << "Here are the marks stored in array" << endl;
    for (int i = 0; i < size; i++)
    {
        cout << marks[i] << endl;
    }
};