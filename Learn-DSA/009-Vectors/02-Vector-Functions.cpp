#include <iostream>
#include <vector>
using namespace std;

int main() {

    vector <int> vec = {1,2,3,4};

    cout << "Size before push_back = " << vec.size() << endl;

    vec.push_back(100); // 100
    
    cout << "Size after push_back = " << vec.size() << endl;


    cout << "Size before push_back = " << vec.size() << endl; // 5

    vec.pop_back(); // 100
    
    cout << "Size after push_back = " << vec.size() << endl; // 4

    cout << vec.front() << endl; // 1

    cout << vec.back() << endl; // 4
    
    cout << vec.at(1) << endl; // 2 --> same as writing as vec[1] 
}