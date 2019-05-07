#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// is value in binary format a palindrome
typedef struct _a {
    char a;
    int count;
} charCountT;

int isAnagram( char *a, char *b )
{
    charCountT countsA[26], countsB[26];
    char *aToz = "abcdefghijklmnopqrstuvwxyz";
    char c, *p, *q;
    int i = 0;
    
    if (strlen(a) != strlen(b)) {
        return 1;
    }
    while ( i < strlen(aToz) ) {
        c = aToz[i];
        countsA[i].a = c;
        countsA[i].count = 0;
        countsB[i].a = c;
        countsB[i].count = 0;
        i++;
    } 
    
    p = a;
    q = b;
    while ( *p != '\0' ) {
        for( i = 0; i < 26; i++ ) {
           if( countsA[i].a == *p ) {
               countsA[i].count++;
               break;
           }
        }
        for( i = 0; i < 26; i++ ) {
           if( countsB[i].a == *q ) {
               countsB[i].count++;
               break;
           }
        }
        p++;
        q++;
    }
    for( i = 0; i < 26; i++ ) {
        if( countsA[i].count != countsB[i].count ) {
            return 1;
        }
    }
    
    return 0; 
}

int main( int argc, char **argv )
{
    unsigned int le;
    int rc;
    if( argc != 3 ) {
        printf("Usage: isAnagram <wordA> <wordB>\n");
        exit(1);
    }

    rc = isAnagram( argv[1], argv[2] );
    if( rc == 0 ) {
        printf("%s, %s are anagrams\n", argv[1], argv[2]);
    } else {
        printf("%s, %s are not anagrams\n", argv[1], argv[2]);
    }
    return 0; 
}
