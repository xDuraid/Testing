#include <iostream>

using namespace std;

// Time Complexity: O(n log(n))
// Space Complexity: O(n)

int binarySearch(int a[], int n, int key)
{
    int left = 0, right = n - 1, middle;
    int ans = -1;
    while(left <= right){
        middle = left + (right - left) / 2;
        if(a[middle] == key){
            ans = middle;
            break;
        }
        else if(a[middle] < key)
            left = middle + 1;
        else
            right = middle - 1;
    }
    return ans;
}

void resultIndices(int a[], int n, int b[], int k)
{
    for(int i = 0; i < k; i++)
        cout << binarySearch(a, n, b[i]) << " ";
}

int main()
{
    int n, k;
    cin >> n;
    int a[n];
    for(int i = 0; i < n; i++)
        cin >> a[i];
    cin >> k;
    int b[k];
    for(int i = 0; i < k; i++)
        cin >> b[i];
    resultIndices(a, n, b, k);
	return 0;
}

