#include <stdlib.h>

int* frequency( char s[] ) {
   int *freq;
   char *ptr;
   freq = (int*)( calloc( 256, sizeof( int ) ) );
   if( freq != NULL )
      for( ptr = s; *ptr; ptr++ )
         freq[ *ptr ] += 1;
   return freq;
}
