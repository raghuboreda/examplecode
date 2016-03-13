#include <stdlib.h>
#include <stdio.h>

char *my_strcpy(char *destination, const char *src)
{
    char *dst = destination;
    while (*src) {
        *dst++ = *src++;
    }
    *dst = '\0';
    return destination; 
}

int my_strlen (const char *source)
{
    int len=0;
    while (*source) {
        *source++;
        len++;
    }
    return len;
}

char *my_strcat(char *s1, char *s2)
{
    char *p = s1;
    while (*s1) {
        *p++ = *s1++;
    }

    while (*s2) {
        *p++ = *s2++;
    }
    *p = '\0';
    return s1; 
}

char *my_strchr (char *s, int c)
{
    char *p = s;
    while (*p) {
        if (*p++ == c) {
            break;
        }
    }
    if (*p == '\0') {
        return NULL;
    }
    return p;
}

void reverseString (char *src, char *dest)
{
    char *head;
    head = src;
    while (*src != '\0') {
        src++;
    }
    src--;
 
    while (src != head) {
        *dest = *src;
        dest++;
        src--;
    }
    *dest = *src;
    dest++;
    *dest = '\0';
}

int isPalindrome (char *src)
{
    int index, length = 0;
    char *head, *tail;
    head = src;
    tail = src;
    while (*tail != '\0') {
        length++;
        tail++;
    }
    tail--;
    length = length/2;
    index = 0;

    while ((*head == *tail) && (index < length)) {
        head++;
        tail--;      
        index++;
    }

    if (index < length ) {
        return 1;
    }
    return 0;
}

int main (int argc, char **argv)
{
    char strA[30] = "You Are my Sun Shine";
    char strB[30] = "Gloria";
    char strC[30];
    char strD[60] = " In every which way";
    char strE[60];
    char *chrptr;

    my_strcpy(strC, strA);
    my_strcat(strD, strA);
    
    printf("strC is %s\nstrB len is %d\nstrD is %s\n",
           strC, my_strlen(strB), strD);

    chrptr = my_strchr(strD, 'w');

    printf("new chrptr is %s\n", chrptr);
    reverseString(strA, strE);
 
    printf("reverse string is %s\n", strE);
    printf("malayalam is %d\n", isPalindrome("malayalam"));
    printf("rajjar is %d\n", isPalindrome("rajjar"));
    printf("babjar is %d\n", isPalindrome("babjar"));
    printf("StuckYkcutS is %d\n", isPalindrome("StuckYkcutS"));
    return 0;
}
