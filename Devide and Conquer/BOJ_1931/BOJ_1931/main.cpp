#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

vector<pair<int,int>> v;
vector<pair<int,int>> r;

bool compare(const pair<int, int>&a, const pair<int, int>&b){
    return a.second < b.second;
}

int main() {
    //input
    int n;
    cin >> n;
    for(int i=0;i<n;i++){
        int tmp1, tmp2;
        cin >> tmp1;
        cin >> tmp2;
        v.push_back(make_pair(tmp1,tmp2));
    }
    
    //sort(v.begin(),v.end());
    sort(v.begin(), v.end(), compare);
    
    /*
    for(int i=0;i<v.size();i++){
        cout << v[i].first << " " << v[i].second << endl;
    }*/
    
    int now_startingTime=v.back().first;
    
    r.push_back(make_pair(v.back().first, v.back().second));
    int i=v.size()-2;
    int count=1;
    
    while(i>=0){
        if(v[i].second<now_startingTime){
            r.push_back(make_pair(v[i].first, v[i].second));
            now_startingTime=v[i].first;
            count++;
        }
        i--;
    }
    /*
    for(int i=v.size()-2;i>=0;i--){
        if(r[i].first!=0&&r[i].second!=0)
            cout << r[i].first << " " << r[i].second << endl;
    }*/
    
    cout << count << endl;
    
    return 0;
}
