#include <stdio.h>
#include <stdlib.h>

typedef struct _ll {
   int value;
   struct _ll *next;
} ll_t, *ll_t_p;

ll_t_p head_ptr = NULL;

void insert( ll_t_p *hd, int value )
{
    ll_t_p tmp_head = hd;
    ll_t_p tmp;
    if( tmp_head == NULL ) {
	tmp = (ll_t *)malloc(sizeof(ll_t));
	tmp->value = value;
	tmp->next = NULL;
	hd = tmp;
	return;
    }

    while( tmp_head->next != NULL ) {
	tmp_head = tmp_head->next;
    }

    tmp = (ll_t *)malloc(sizeof(ll_t));
    tmp->value = value;
    tmp->next = NULL;
    tmp_head->next = tmp;
    return;
}

void print_ll( void )
{
    ll_t_p tmp_head = head_ptr;
    if( tmp_head == NULL ) {
	printf("No elements in LL\n");
	return;
    }

    while( tmp_head != NULL ) {
	printf("Values are %d\n", tmp_head->value);
	tmp_head = tmp_head->next;
    }
    return;
}

bool search( ll_t_p *head, int value )
{
    while (head != NULL && head->next != NULL) {
	if (head->value == value) {
	    return 1;
	}
    }
    if (head != NULL && head->value == value) {
	return 1;
    }
    return 0;
}

void removeDups( void )
{
     ll_t_p tmp_head=NULL;
     ll_t_p traverse_head = head_ptr;
     while (traverse_head != NULL) {
	 if (search(tmp_head, traverse_head->value) == 0) {
	     insert(tmp_head, traverse_head->value); 
         }
     }
}

int main( int argc, char **argv )
{
    int i;
    int a[10] = { 1, 2, 3, 1, 5, 6, 2, 3, 2, 10 };
    for( i=0; i < 10; i++ ) {
        insert( &head_ptr, a[i] );	
    }

    print_ll();
    return 0;
}

