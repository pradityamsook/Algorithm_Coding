#include <iostream>
#include<cstdlib>
using namespace std;

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



int main()
{
  int array[100], n, c, d, swap,x;
 
  cout<<"Enter number of elements :";
  cin>>n;
 
  cout<<"Enter integers: "<<n<<endl;
 
  for (c = 0; c < n; c++)
    cin>>array[c];
 
  for (c = 0 ; c < ( n - 1 ); c++)
  {
    for (d = 0 ; d < n - c - 1; d++)
    {
      if (array[d] > array[d+1]) /* For decreasing order use < */
      {
        swap       = array[d];
        array[d]   = array[d+1];
        array[d+1] = swap;
      }
    }
  }
 
  cout<<"Sorted list in ascending order: "<<endl;
 
  for ( c = 0 ; c < n ; c++ )
 	
     cout<<array[c]<<endl;
     cout<<" Enter the element to be search > ";
     cin>>x;
     binary_search(array,n,x);
 
  return 0;
}
