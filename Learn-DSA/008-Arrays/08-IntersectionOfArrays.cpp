#include <iostream>
using namespace std;

int main()
{
    int arr1[] = {1, 2, 3, 4, 7, 100};
    int arr2[] = {11, 100, 4, 7, 1};
    int arr1Size = sizeof(arr1) / sizeof(int);
    int arr2Size = sizeof(arr2) / sizeof(int);

    for (int i = 0; i < arr1Size; i++)
    {
        bool isCommon = false;
        for (int j = 0; j < arr2Size; j++)
        {
            if (arr1[i] == arr2[j])
            {
                isCommon = true;
            }
        }
        if (isCommon)
        {
            cout << arr1[i] << endl;
        }
    }
}