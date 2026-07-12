### 1. Pair Sum

- Return pair in a sorted array with the target sum.
- Only a unique pair will be the solution.

##### Approach

1. Brute force - _Check for all the pair with the target sum_ --> O(n\*\*2)
2. Optimal - **2 Pointer Approach** [because it is a sorted array] --> O(n)
   - pairSum > targetSum --> end--
   - pairSum < targetSum --> start++
   - pairSum = targetSum --> return

### 2. Majority Element

- Return element which comes > `floor(n/2)` times
- array may not be sorted

##### Approach

1. Brute Force - _Check of all the element with double loop_ --> `O(n\*\*2)`
2. Optimal w/ Sorting - _Sort the array and then use 1 loop_ --> `O(nlog(n)+n)`
3. Moore's Voting Algo --> `O(n)`
   - same element --> `freq++`
   - different element --> `freq--`
   - when `freq == 0` --> assign the num (`ans = arr[i]`)
