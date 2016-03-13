#include <stdio.h>
int insertionSort( int *a, int size ) 
{
    int j = 1, temp;
    int i = 0;
    while ( j < size) {
        i = j - 1;
        while ( i >= 0 ) {
            if (*(a+i) > *(a+i+1)) {
                temp = *(a+i); //example of pointer arithmetic
                a[i] = a[i+1]; //example of array access
                a[i+1] = temp;
            }
            i = i - 1;
        }
        j = j + 1;
    }
    return 0;
}

int main( int argc, char *argv[] )
{
    int listA[] = { 3, 127, 105, 101, 81 };
    int i = 0;
    int listSize = (sizeof(listA)/sizeof(int));
    insertionSort( listA, listSize );
    for( i=0; i < listSize; i++ ) {
         printf("%d, ", listA[i]);
    }
    printf("\n");
    return(0); 
}

