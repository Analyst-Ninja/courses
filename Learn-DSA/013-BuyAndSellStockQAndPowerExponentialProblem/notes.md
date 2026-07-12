## Power Exponential Problem

### Compute x^n - using Binary Exponentiation

- Binary form of any number n: <= `log2(n) + 1`
- Hence the logic is: We loop on the binary form of n
- As the number of digits/ bits in binary form will always be <= `log2(n) + 1`, Hence the time complexity will be reduced to `O(log(n))`

##### Steps to solve this problem

1. Convert the power `n` in its binary form
2. We will get the `x^n` for different `n` and get the square of it to get higher power
3. But we will assign only when we get the `1` in the binary form - i.e. `n % 2 == 1`

```c++
class Solution {
public:
    double myPow(double x, int n) {
        long binForm = n;
        double ans=1;
        // Handling the edge cases
        if (binForm == 0) return 1.0;
        if (binForm == 1) return x;

        // If the power is negative
        if (binForm < 0){
            binForm = -binForm;
            x = 1/x;
        }
        while (binForm > 0){
            // Only assiging the ans when 1 comes in the binary form
            if (binForm % 2 == 1){
                ans *= x;
            }
            // Updating the x by multiplying itself and the binaryForm everytime
            x *= x;
            binForm /= 2;
        }
        return ans;
    }
};
```

## Stock Buy and Sell problem

Steps to solve this

1. initialize `maxProfit = 0` and `bestBuy = arr[0]` - the first element of arr
2. if the `arr[i] <= bestBuy` then we don't have to change anything
3. else
   - maxProfit -> `max(maxProfit, (arr[i] - bestBuy))`
   - bestBuy -> `min(bestBuy, arr[i])`

```c++
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int bestBuy = prices[0];
        int maxProfit = 0;

        for (int i=1; i<prices.size(); i++){
            // Check for the maximum profit
            if (prices[i] > bestBuy){
                maxProfit = max(maxProfit, (prices[i] - bestBuy));
            }
            // Checking for best Buy or the minimum value to buy the stock for
            bestBuy = min(bestBuy, prices[i]);
        }
    return maxProfit;
    }
};
```
