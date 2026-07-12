#include <iostream>
using namespace std;

int linearSearch(int array[], int target, int arrSize) {

    for(int i = 0; i < arrSize; i++) {
        if(array[i] == target) return i; //Found
    }

    return -1; //Not Found
}


int main() {
    int arr[] = {1,2,34,45,5,8};
    int size = sizeof(arr)/sizeof(int);
    int valueToSearch = 45;
    int resultIndex;

    resultIndex = linearSearch(arr, valueToSearch, size);
    
    cout << "Index : " << resultIndex << endl;;
}