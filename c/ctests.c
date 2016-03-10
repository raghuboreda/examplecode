#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void beOrLe( void )
{
    unsigned int value = 0x12345678;
    unsigned char *a;
    a = (unsigned char *)&value;
    if ( *(unsigned char *) a == 0x12 ) {
       printf( "Big Endian\n");
    } else if ( *(unsigned char *) a == 0x78 ) {
       printf( "Little Endian\n");
    } else {
       printf( "Unknown Architecture\n");
    }
}

#define BeToLe(x) (((x & 0xff) << 24) | ((x & 0xff00) << 8) | \
                   ((x & 0xff0000) >> 8 ) | ((x & 0xff000000) >> 24)) 

// is value in binary format a palindrome
int isPalindrome( unsigned int value )
{
    int maxBitPos=0, index=0;
    unsigned char bitValues[ 32 ];

    for( maxBitPos=31; maxBitPos >= 0; maxBitPos-- ) {
        if( value & (1<<maxBitPos) ) 
            break;
    }

    for( index=0; index <= maxBitPos; index++ ) {
        if( value & (1 << index )) {
            bitValues[index] = 1;
        } else { 
            bitValues[index] = 0;
        }
    }
 
    index = 0; 
    while( bitValues[index] == bitValues[maxBitPos-index] ) {
        if( index > maxBitPos/2 )
            return 1;
        index++;
    }
    return 0;        
}

int main( int argc, char **argv )
{
    unsigned int le;
    int rc;

    if( strcmp(argv[1], "beToLe") == 0 ) {
        le = (unsigned int)strtoul(argv[2], NULL, 0);
        printf("value 0x%x Le 0x%x\n", le, BeToLe(le));
    } else if( strcmp(argv[1], "isBe") == 0 ) {
        beOrLe();
    } else if( strcmp(argv[1], "isPal") == 0 ) {
        le = (unsigned int)strtoul(argv[2], NULL, 0);
        rc = isPalindrome( le );
        if( rc == 0 ) {
            printf("%d is not binary Palindrome\n", le);
        } else {
            printf("%d is binary Palindrome\n", le);
        }  
    }
    return 0; 
}
