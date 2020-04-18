#include <bits/stdc++.h>
using namespace std;

void add(int *x, int *y){
    int sum = *x + *y;

    int  Diff = abs(*x - *y);

    cout<<sum<<"\n";

    cout<<Diff;
}

int  main(){

    int a,b;

   

    cin>>a>>b;

    add(&a, &b);

}
