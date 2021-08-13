#include <iostream>
using namespace std;

int main() {
    int arr[200][200];
    int d[200];
    int v[200];
    int nv,ne,s,tmin;
    int a,b;

    //1
    cin >> nv;
    cin >> ne;
    cin >> s;
    cout << nv << ne << s << endl;
    for(int i=0;i<nv;i++){
        for(int j=0;j<nv;j++)
            arr[i][j]=-1;   //set INF
    }
    for(int i=0;i<ne;i++){
        cin >> a;
        cin >> b;
        cin >> arr[a-1][b-1];
    }
    //2
    d[0]=s;
    for(int i=0;i<nv;i++){
        d[i]=arr[s][i];
    }
    //3
    //4
    for(int i=0;i<nv;i++){
        for(int j=0;j<nv;j++){
            cout << arr[i][j] << " ";
        }
        cout << endl;
    }
}
