#include <iostream>
#include <climits>
using namespace std;

int main() {
    int arr[5] = {100, 99, 78, -2, 23};
    int size = sizeof(arr)/sizeof(int);
    int smallest = INT_MAX;
    int largest = INT_MIN;
    int largestValueIndex = 0;
    int smallestValueIndex = 0;


    for(int i = 0; i < size; i++){
        // if (arr[i] < smallest) {
        //     smallest = arr[i];
        // }

        smallest = min(arr[i], smallest);
        largest = max(arr[i], largest);
    }

    for(int i = 0; i < size; i++) {
        if (smallest == arr[i]) smallestValueIndex = i;
        if (largest == arr[i]) largestValueIndex = i;
    }

    cout << "Largest Value: " << largest << " @ Index: " << largestValueIndex << endl;
    cout << "Smallest Value: " << smallest << " @ Index: " << smallestValueIndex << endl;
    

    return 0;
}