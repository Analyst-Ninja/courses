#include <iostream>
using namespace std;

void printArr(int arr[], int size)
{

    for (int i = 0; i < size; i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;
}

// 2 pointer approach
void reverseArr(int arr[], int size)
{
    int start = 0;
    int end = size - 1;

    while (start < end)
    {
        swap(arr[start], arr[end]);
        start++;
        end--;
    };
}

int main()
{
    int arr[5] = {1, 2, 3, 4, 5};

    int arrSize = sizeof(arr) / sizeof(int);

    cout << "Original Array:- " << endl;
    printArr(arr, arrSize);

    reverseArr(arr, arrSize);

    cout << "Reversed Array:- " << endl;
    printArr(arr, arrSize);
}