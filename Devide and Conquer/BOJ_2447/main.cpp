
#include <iostream>
using namespace std;
int star[6500][6500];

void draw(int n, int x, int y){
    if(n==3){
        star[x][y]=1;
        star[x+1][y]=1;
        star[x+2][y]=1;
        
        star[x][y+1]=1;
        star[x+1][y+1]=0;
        star[x+2][y+1]=1;
        
        star[x][y+2]=1;
        star[x+1][y+2]=1;
        star[x+2][y+2]=1;
        
        return;
    }
    int nn=n/3;
    draw(nn,x,y);
    draw(nn,x+nn,y);
    draw(nn,x+2*nn,y);
    
    draw(nn,x,y+nn);
    //draw(nn,x+nn,y+nn);
    
    draw(nn,x+nn+nn,y+nn);
    
    draw(nn,x,y+2*nn);
    draw(nn,x+nn,y+2*nn);
    draw(nn,x+nn+nn,y+2*nn);
}

int main() {
    int n;
    
    cin >> n;
    draw(n,0,0);
    
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            if(star[i][j]==1)printf("*");
            else printf(" ");
        }
        printf("\n");
    }
    
    return 0;
}
