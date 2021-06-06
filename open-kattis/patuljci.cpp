#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    vector<int> nums={};
    int x=0;
    int sum=0;
    for (int i = 0; i < 9; i++)
    {
        cin >> x;
        nums.push_back(x);
        sum += x;
    }
    vector<int> sorted = nums;
    sort(sorted.begin(), sorted.end());

    sum -= 100;

    auto it1 = sorted.begin();
    auto it2 = sorted.end() - 1;

    while (*it1 + *it2 != sum)
    {
        if (*it1 + *it2 < sum)
            it1++;
        if (*it1 + *it2 > sum)
            it2--;
    }
    for (int i = 0; i < 9; i++)
    {
        if (nums[i] != *it1 && nums[i] != *it2)
            cout << nums[i] << "\n";
    }
    return 0;
}