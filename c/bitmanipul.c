#include <stdio.h>
#include <stdlib.h>

unsigned short bit_multiply (unsigned char a, unsigned char b)
{
    unsigned short csum, jsum;
    unsigned char index, jindex; 
    csum = 0; 
    jsum = 0; 
    for (index=0; index < 8; index++) {
        jsum = 0;
        if (b & (1 << index)) { /* bit is 1 */
            for (jindex=0;jindex < 8;jindex++) {
                if (a & (1 << jindex)) { /* bit is 1 */
                    jsum += (1<<jindex);
                }
            }
            csum = csum + (jsum << index);
        }
    }
    return csum; 
}

int main (int argc, char **argv)
{
    unsigned char a = 5, b = 10;
    unsigned short c;
    c = bit_multiply(a,b);
    printf("result is %u\n", c);
    c = bit_multiply(9,19);
    printf("result is %u\n", c);
    c = bit_multiply(25,25);
    printf("result is %u\n", c);
    c = bit_multiply(254,253);
    printf("result is %u\n", c);
    return 0;
}
