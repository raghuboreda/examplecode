#include <stdio.h>
#include <stdlib.h>
#include <string.h>
/*
 * int *b, c[], *(*d[])();
 * d is array of pointers to functions returning int pointers
 * how to allocate memory for pointer-vector array.
 * int ***array;  10*20*30 
 * array = (int ***)malloc(10*sizeof(int **));
 *  
 * for(j=0; j<20; j++) {
 *    *(array+j) = (int **)malloc(20*sizeof(int *));
 * }
 * for(k=0; k < 10; k++) {
 *    for (j=0; j < 20; j++) {
 *       *(*(array+k)+j) = (int *)malloc(30*sizeof(int));
 * **array
 */
/*
 * basic link list addition
 * and deletion
 */

typedef struct _ll
{
   int value;
   struct _ll *next;
} ll_t;

void add_element(ll_t **hdr, int value)
{
   ll_t *ptr;
   if (*hdr == NULL) {
      *hdr = (ll_t *)malloc(sizeof(ll_t));
      ptr = *hdr;
      ptr->value = value;
      ptr->next = NULL;
      return;
   }
   ptr = *hdr;

   while (ptr->next != NULL) {
      ptr = ptr->next;
   }
   ptr->next = (ll_t *)malloc(sizeof(ll_t));
   ptr = ptr->next;
   ptr->value = value;
   ptr->next = NULL;
   return;
}

void delete_element(ll_t **hdr, int value)
{
   ll_t *ptr, *prev_ptr;
   if (*hdr == NULL) {
      return;
   }
   ptr = *hdr;
   prev_ptr = *hdr;
   while (ptr->next != NULL && ptr->value != value) {
      prev_ptr = ptr;
      ptr = ptr->next;
   }
   if (ptr->next == NULL) {
      if (ptr->value == value) {
	 prev_ptr->next = NULL;
	 free(ptr);
	 return;
      } else {
	 printf("value not found Nothing to delete\n");
      } 
   } else {
      if (ptr == *hdr) {
	 prev_ptr = ptr->next;
	 *hdr = prev_ptr;
      } else {
         prev_ptr->next = ptr->next;
      }
      free(ptr);
   }
   return;
}
/*
 * remove duplicates
 * O(1) space and O(n**2) time
 */
int remove_duplicates(ll_t **hdr) {
   ll_t *ptr;
   ptr = *hdr;
   if (*hdr == NULL || ptr->next == NULL) {
      return 0;
   }
   ll_t *runner, *prev;
   while( ptr->next != NULL ) {
      runner = ptr->next;
      prev = ptr;
      while( runner != NULL) {
	 if( runner->value == ptr->value ) {
             prev->next = runner->next;	
             free(runner);
	     runner = prev->next;
	 } else {
	     prev = runner;
	     runner = runner->next;
	 }
      }
      ptr = ptr->next;
   }
}
/*
 * kthToLast Element in linked list
 */
int kth_to_last(ll_t **hdr, int k)
{
   ll_t *ptr1, *ptr2;
   ptr1 = *hdr;
   ptr2 = *hdr;
   int i = 0;
   while (ptr2 != NULL && (i<k) ) {
      ptr2 = ptr2->next;
      i = i + 1;
   }
   if (ptr2 == NULL) {
      return 0;
   }
   while (ptr2 != NULL) {
      ptr1 = ptr1->next;
      ptr2 = ptr2->next;
   }
   return ptr1->value;
}   
/*
 * delete middle node
 */
int delete_node( ll_t **node )
{
   ll_t *ptr, *prev_ptr;
   ptr = *node;
   prev_ptr = ptr->next;
   /*
   ptr->value = ptr->next->value;
   ptr->next = ptr->next->next;
   */
   memcpy(*node,ptr->next,sizeof(ll_t)); 
   free(prev_ptr);
}

int main(int argc, char *argv[])
{
   ll_t *hdr, *ptr;
   hdr = NULL;
   for (int i=1;i < 11;i++) {
      add_element(&hdr, i);
   }
   delete_element(&hdr, 5);
   delete_element(&hdr, 10);
   delete_element(&hdr, 1);
   for (int i=21;i < 25;i++) {
      add_element(&hdr, i);
   }
   add_element(&hdr, 21);
   add_element(&hdr, 22);
   add_element(&hdr, 10);
   add_element(&hdr, 21);
   add_element(&hdr, 9);
   add_element(&hdr, 22);
   add_element(&hdr, 23);
   add_element(&hdr, 23);
   add_element(&hdr, 28);
   remove_duplicates(&hdr);
   ptr = hdr;
   int del_j = 0;
   while (ptr->next != NULL) {
      ptr = ptr->next;
      del_j += 1;
      if (del_j == 3) {
	 delete_node(&ptr);
	 break;
      }
   }
   ptr = hdr;
   while (ptr->next != NULL) {
      printf("values are %d\n", ptr->value);
      ptr = ptr->next;
   }
   printf("values are %d\n", ptr->value);

   printf("2nd to last is %d\n", kth_to_last(&hdr, 2));
   printf("4th to last is %d\n", kth_to_last(&hdr, 4));
   return 0;
}
