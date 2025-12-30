#include <bits/stdc++.h>

using namespace std;

int main(){
    int n;
    string s;

    cin >> n >> s;

    vector<int> cnt(3, 0);
    for (char c : s) cnt[c - '0']++;

   
    cout << endl;
    return 0;
}