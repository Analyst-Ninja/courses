#include <iostream>
using namespace std;

double myPow(double x, int n)
{
    long binForm = n;
    double ans = 1;
    if (n == 0)
        return 1.0;
    if (n == 1)
        return x;
    if (n < 0)
    {
        x = 1 / x;
        binForm = -binForm;
    }
    while (binForm > 0)
    {
        if (binForm % 2 == 1)
            ans *= x;
        x *= x;
        binForm /= 2;
    }
    return ans;
}

int main()
{

    int x = 10, n = 1;
    double ans;
    ans = myPow(x, n);
    cout << ans << endl;
}