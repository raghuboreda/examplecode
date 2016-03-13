#include <stdio.h>
#include <stdlib.h>

unsigned int strtoint (char *a)
{
    int index = 1;
    unsigned int csum = 0;
    unsigned char k;
    char *b = a;
    while (*b != '\0') {
        b++;
    }
    b--;
    /* Now b points to tail-1 */
    while (b != a) {
        k = *b;
        csum = csum + (int)((k-'0')*(index));
        index = index*10;
        b--;
    }
    k = *b;
    csum = csum + (int)((k-'0')*(index));
    return csum;
}

void inttostr (int a, char *s)
{
    sprintf(s, "%d",a);
}

void inttostr1 (int a, char *s)
{
     int index = 1, c = 0;
     while (index < a) {
         index = index * 10;
     }
     while (index != 1) {
         index = index/10;
         c = a/index;
         *s = (char)(c+'0');
         a = a%index;
         s++;
     }
     *s='\0';
}

int main (int argc, char **argv)
{
    unsigned int sum;
    char str[80];
    sum = strtoint("567890"); 
    printf("sum is %d\n", sum);
    sum = strtoint("890876543"); 
    printf("sum is %d\n", sum);
    sum = strtoint("13"); 
    printf("sum is %d\n", sum);
    inttostr(13, str); 
    printf("string is %s\n", str);
    inttostr(890876543, str); 
    printf("string is %s\n", str);
    inttostr1(435, str); 
    printf("string is %s\n", str);
    return 0;
}
