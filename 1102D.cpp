#include <bits/stdc++.h>

using namespace std;

int main(){
    int n;
    string s;

    cin >> n >> s;

    vector<int> cnt(3, 0);
    for (char c : s) cnt[c - '0']++;
    
    int need = n / 3;

    //Left pass
    for (int i = 0; i < n; i++){
        int d = s[i] - '0';
        if (cnt[d] > need){
            for (int x = 0; x < d; x++){
                if (cnt[x] < need ){
                    cnt[d]--;
                    cnt[x]++;
                    s[i] = char('0' + x);
                    break;
                }
            }
        }
    }

    //Right Pass

    for (int i = n-1; i>=0; i--){
        int d = s[i] - '0';
        if (cnt[d] > need){
            for (int x = 2; x > d; x--){
                if (cnt[x] < need){
                    cnt[d]--;
                    cnt[x]++;
                    s[i] = char('0' + x);
                    break;
                }
            }
        }
    }
   
    cout << s << endl;

    return 0;
}