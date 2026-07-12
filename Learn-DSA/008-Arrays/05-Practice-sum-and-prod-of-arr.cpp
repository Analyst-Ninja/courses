#include <iostream>
using namespace std;

int main()
{
    int arr[] = {1, 2, 3, 4, 5};
    int size = sizeof(arr) / sizeof(int);
    int sum = 0;
    int prod = 1;
    for (int i = 0; i < size; i++)
    {
        prod *= arr[i];
        sum += arr[i];
    }

    cout << "Array Sum: " << sum << endl;
    cout << "Array Product: " << prod << endl;
}