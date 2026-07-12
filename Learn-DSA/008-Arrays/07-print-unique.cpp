#include <iostream>
#include <climits>
using namespace std;

int main()
{
    int arr[] = {1, 2, 22, 3, 1, 1, 1, 1, 56};
    int arrSize = sizeof(arr) / sizeof(int);

    for (int i = 0; i < arrSize; i++)
    {
        bool isUnique = true;
        for (int j = 0; j < arrSize; j++)
        {
            if (i != j && arr[i] == arr[j])
            {
                isUnique = false;
            }
        }
        if (isUnique == true)
        {
            cout << arr[i] << endl;
        }
    }
}