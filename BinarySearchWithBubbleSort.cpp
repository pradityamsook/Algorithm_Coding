#include <iostream>
#include <cstdlib>
using namespace std;

/* function bubble sort for sort of binary before seach*/
int bubble_sort(int arr[],int n){
    int i,j,t;
    for(i = n-2;i>=0;i--)
     for(j=0;j<=i;j++){
        if(arr[j] > arr[j+1]){
            t = arr[j];
            arr[j] = arr[j+1];
            arr[j+1] = t;
        }
    }
}

int binary_search(int arr[],int n,int x){
    int left,right,mid;
    left = 0;
    right = n-1;

    while(left <= right){
        mid = (left + right)/2; //formula to find mid
        if(x == arr[mid])
         break;
        if(x > arr[mid])
         left = mid +1;
        else
         right = mid - 1;
    }

    if(left>right){
    	cout<<endl;
     	cout<<x<<" Element not found !!!";
	}
    
    else{
    	cout<<endl;
    	cout<<x<<" Element is found at "<<mid+1<<" position";
     	
	}
     
}

int main(){
	int j;
    int i,x,n;
    cout<<endl;
    cout<<" Enter number of array for search > ";
    cin>>j;
    int arr[j];
    cout<<endl;
    cout<<" Enter the number of elements > ";
    cin>>n;
    cout<<endl;
    cout<<" Enter the element > ";
    for(i = 0;i<n;i++){
    	cin>>arr[i];  	
    	cout<<" Enter the element to be search > ";
    	cin>>x;
    	bubble_sort(arr,n); //function call
    	binary_search(arr,n,x);
	}
     
    
    
     
    
    

}
