#include <iostream>
using namespace std;

// Check Prime or Not
string checkPrime(int N) {

    for (int i = 2; i*i <= N; i++){
        if (N % i == 0) {
            return "Not Prime";
        }
    }

    return "Prime";
}

// Print Prime Numbers
int printPrimeNums(int N) {

    for(int i = 2; i <= N; i++) {
        
        if (checkPrime(i) == "Prime") {
            cout << i << " ";
        }
    }

    return 0;
}

// Print Fibbonacci Series
int printFibb(int N) {

    int num1 = 0;
    int num2 = 1;
    int temp;
    for (int i = 0; i < N; i++) {
        if (i == 0) {
            cout << 0 << " ";
        }
        else if (i == 1) {
            cout << 1 << " ";
        }
        else {
            cout << num1 + num2 << " ";
            temp = num1;
            num1 = num2;
            num2 = temp + num2;
        }
    }
    return 0;
}



int main() {

    // Invoking CheckPrime Function
    int N = 20;
    cout << N << " = " << checkPrime(N) << endl;

    // Invoking printPrimeNums Function
    cout << N << " = ";
    printPrimeNums(N);
    cout<< endl;

    // Invoking Fibbonacci Function
    cout << N << " = ";
    printFibb(N);
    cout << endl;

    return 0;
}
