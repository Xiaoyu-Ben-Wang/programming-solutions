#include <iostream>
#include <map>
using namespace std;

int main()
{
    int n;
    cin >> n;
    map<int, int> m;
    for (int i = 0; i < n; i++)
    {
        int d, t;
        cin >> d >> t;
        m[t] += 1;
        m[t - d] += 1;
        m[t - 2 * d] += 1;
    }
    int max = 0;
    for (auto it = m.begin(); it != m.end(); it++)
        if (it->second > max)
            max = it->second;
    cout << (max + 1) / 2;
}