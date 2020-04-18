#include<bits/stdc++.h>
using namespace std;

int main(){
    int  temp,min,loc;
    // cout<<"enter the size of array";
    
    int A[10];
    //cout<<"enter the array";
    for(int i=0 ; i<4;i++){
        cin>>A[i];
    }

for ( int i=0 ; i<3; i++){

    min =A[i];
    loc=i;

    for(int j=i+1; j<4;j++){
        if(A[j]<min){
            min=A[j];
            loc=j;
        }
    }

    temp=A[i];
    A[i]=A[loc];
    A[loc]=temp;
}



cout<<A[3];

}