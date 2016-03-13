#include <stdio.h>
#include <stdlib.h>

const char *cis452_name = "CIS452";
const int CIS452_LIMIT = 0xdeadbeef;
const char *cis452_nom = "See Me?";

int cis452_global1;
int cis452_global2 = 0;
int cis452_global3 = 123;

void cis452_do_nothing()
{
    printf("I'm doing nothing\n");
}

int main()
{
    int cis452_local1;

    cis452_local1 = 50;
    printf("Hello from %d\n", getpid());
    return 0;
}
