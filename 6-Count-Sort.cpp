#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

void count_sort(vector<int>a, int min,int max){
    vector<int>freq((max-min+1),0);
    // cout<<max<<min;
    for(int i=0;i<a.size();i++){
        freq[a[i]-min]++;
    }
    int j=0,k=0;
    while(k<freq.size()){
        while(freq[k]>0){
            a[j++]=min+k;
            freq[k]--;
        }
        k++;
    }

    for(int i=0;i<a.size();i++)
    cout<<a[i]<<" ";


    //The time complexity of count sort is O(N + K), where N is the size of the input array and K is the range of the array i.e the largest element of the array.
}

int main(){
    cout<<"Enter size: \n";
    int n;
    cin>>n;
    vector<int> a(n);
    cout<<"Enter elements: \n";
    for(int i=0;i<n;i++){
        cin>>a[i];
    }
    
    // cout<<endl<<*max_element(a.begin(),a.end())<<endl<<*min_element(a.begin(),a.end())<<endl;

    count_sort(a,*min_element(a.begin(),a.end()),*max_element(a.begin(),a.end()));
}