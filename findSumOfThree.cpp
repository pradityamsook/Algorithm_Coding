#include <iostream>
#include "bits/stdc++.h"
using namespace std;

bool FindSumOfTwo(vector<int> &A, int val, size_t startIndex)
{
    for (int i = startIndex, j = A.size() - 1; i < j;)
    {
        int sum = A[j] + A[i];
        if (sum == val)
        {
            return true;
        }

        if (sum < val)
        {
            ++i;
        }
        else
        {
            --j;
        }
    }
    return false;
}

bool FindSumOfThree(vector<int> arr, int requiredSum)
{
    std::sort(arr.begin(), arr.end());

    for (int i = 0; i < arr.size() - 2; ++i)
    {
        int remainingSum = requiredSum - arr[i];
        if (FindSumOfTwo(arr, remainingSum, i + 1))
        {
            return true;
        }
    }
    return false;
}

int main()
{
    vector<int> arr = {-25, -10, -7, -3, 2, 4, 8, 10};
    for (int i = 0; i < arr.size(); i++)
    {
        cout << arr[i] << " : " << FindSumOfThree(arr, arr[i]) << endl;
    }

    return 0;
}