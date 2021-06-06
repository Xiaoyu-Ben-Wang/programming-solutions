// https://open.kattis.com/problems/ants
#include <iostream>
#include <vector>
#include <climits>
using namespace std;

int main(int argc, char const *argv[])
{
    int c;
    cin >> c;
    for (int i = 0; i < c; i++)
    {
        int l, ants;
        vector<int> pos;
        cin >> l >> ants;
        for (int i = 0; i < ants; i++)
        {
            int t;
            cin >> t;
            pos.push_back(t);
        }
        int min_time = INT_MIN, max_time = INT_MIN;
        for (int i = 0; i < ants; i++)
        {
            if (pos[i] <= l / 2)
            {
                if (pos[i] > min_time)
                {
                    min_time = pos[i];
                }
            }
            else
            {
                if (l - pos[i] > min_time)
                {
                    min_time = l - pos[i];
                }
            }
            if (l - pos[i] > max_time)
            {
                max_time = l - pos[i];
            }
            if (pos[i] > max_time)
            {
                max_time = pos[i];
            }
        }
        cout << min_time << " " << max_time << endl;
    }

    return 0;
}