#include <stdlib.h>
#include <stdio.h>
/*
 * This program illustrate's C's pass by value
 */
int sum (int x, int y)
{
    x = x + y;
    return x;
}
/*
 * This function illustrate's C's simulated pass by reference
 * using pointers
 */
int sump (int *x, int *y)
{
    *x = (*x) + (*y);
    return ((*x));
}

int main (int argc, char **argv)
{
    int a = 4, b = 5, c = 14, d = 15, r, s;
    s = sum(a,b); 
    r = sump(&c, &d);
    printf("a=%d, b=%d s=%d\n",a, b, s);
    printf("c=%d, d=%d r=%d\n",c, d, r);
    return 0;
}
