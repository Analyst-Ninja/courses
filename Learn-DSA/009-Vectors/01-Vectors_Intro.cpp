#include <iostream>
#include <vector>
using namespace std;

// Vectors are dynamic in nature unlike Arrays

int main()
{
    // vector <int> vec; // 0
    // vector <int> vec = {1,2,3}; // 3
    vector<int> vec(3, 0); // 3 values all of them will be 0
    vector<char> vec2 = {'a', 'b', 'c'};
    // cout << vec[0] << endl;
    // cout << vec[1] << endl;
    // cout << vec[2] << endl;

    // for each loop ==>  Specially for vectors --> Just like for in in python

    for (char val : vec2)
    {

        cout << val << " ";
    }
    cout << endl;
}

// To run the code --> g++ -std=c++11 app.cpp && ./a.out