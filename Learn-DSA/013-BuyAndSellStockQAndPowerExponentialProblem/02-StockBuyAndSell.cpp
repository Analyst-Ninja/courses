#include <iostream>
#include <vector>
using namespace std;

int getMaxProfit(vector<int> &prices)
{
    int maxProfit = 0, bestBuy = prices[0];
    for (int i = 1; i < prices.size(); i++)
    {
        if (prices[i] > bestBuy)
        {
            maxProfit = max(maxProfit, (prices[i] - bestBuy));
        }
        bestBuy = min(bestBuy, prices[i]);
    }
    return maxProfit;
}

int main()
{
    int ans;
    vector<int> prices = {7, 1, 5, 3, 6, 4};
    ans = getMaxProfit(prices);
    cout << ans << endl;
    return ans;
}