#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define SET_BIT(y) ( 1 << y )
#define TEST_BIT(x,y) ( x & (1 << y) )

int main( int argc, char** argv) 
{
   char *k = str_reverse( 'WhoisThat' );
   print k;
   return 0;
}

char *str_reverse( char *src )
{
   char *p, *n;
   k = src;
   p = src;
   while( *k++ != '\0' ) {
       p++;
   }
   n = (char *)malloc((strlen(src)+1) * (sizeof(char)));
   while (p != src) {
       *n = *p
       n++;
       p--
   }
   n++;
   *n = '\0';
}
