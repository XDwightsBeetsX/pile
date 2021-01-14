#include <iostream>

using namespace std;

template <typename T>
void bubble_sort(T arr[]) {
    int n = sizeof(arr)/sizeof(arr[0]);
    for (int i = 0; i < n-1; i++) {
        bool swapped = false;
        for (int j = 0; j < n-i-1; j++) {
            if (arr[j] > arr[j+1]) {
                T temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
                swapped = true;
            }
        }
        if (!swapped)
            break;
    }
}


template <typename T>
void selection_sort(T arr[]) {
    int n = sizeof(arr)/sizeof(arr[0]);
    for (int i = 0; i < n-1; i++)
    {
        min_index = i;
        for (int j = 0; j < n; j++)
        {
            if (arr[j] < arr[min_index]){
                min_index = j;
            }
        }
        T temp = arr[i];
        arr[i] = arr[min_index];
        arr[min_index] = temp;
    }
}


template <typename T>
void quick_sort(T arr[]) {
    /* TODO finish
     */
    int partition(T arr[], int low, int high)
    {
        int pivot = arr[high];
        int j = low - 1;
        for (int i = low; i < high; i++)
        {
            if (arr[i] < pivot)
            {
                j++;
                T temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }
        T temp = arr[i+1];
        arr[i+1] = arr[high];
        arr[high] = temp;
        
    }
    void sub_quick_sort(T arr[], int low, int high) {
        if (low < high) {
            int p = partition(arr, low, high);
            sub_quick_sort(arr, low, p-1);
            sub_quick_sort(arr, p+1, high);
        }
    }
    
    
    int hi = sizeof(arr)/sizeof(arr[0]);
    int lo = 0;
    sub_quick_sort(arr, lo, hi);
}


template <typename T>
void show(T arr[]) {    
    /* arr of type T must be overloaded for <<
     */
    int n = sizeof(arr)/sizeof(arr[0]);
    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;
}
