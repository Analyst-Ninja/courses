#include <iostream>
#include <climits>
using namespace std;

int main()
{
    int arr[5] = {1, 2, 5, 3, 4};
    int arrSize = sizeof(arr) / sizeof(int);
    int smallest = INT_MAX;
    int largest = INT_MIN;
    int smallestIndex;
    int largestIndex;

    for (int i = 0; i < arrSize; i++)
    {
        if (arr[i] < smallest)
        {
            smallest = arr[i];
            smallestIndex = i;
        }
        if (arr[i] > largest)
        {
            largest = arr[i];
            largestIndex = i;
        }
    }
    swap(arr[smallestIndex], arr[largestIndex]);

    for (int i = 0; i < arrSize; i++)
    {
        cout << arr[i] << endl;
    }
}