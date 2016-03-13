#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#define SET_BIT(y) ( 1 << y )
#define TEST_BIT(x,y) ( x & (1 << y) )

char *str_reverse( char *src )
{
   char *p, *dest, *k;
   dest = (char *)malloc((strlen(src)+1) * (sizeof(char)));
   k = dest;
   p = src + strlen(src);
   while (p != src) {
       *k = *p;
       k++;
       p--;
   }
   *k = *p;
   k++;
   *k = '\0';
   return dest;
}

int main( int argc, char** argv) 
{
   char *k = str_reverse( "WhoisThat" );
   printf("%s\n", k);
   return 0;
}

