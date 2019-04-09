%module freq
%typemap(out) int* {
   int i;
   $result = PyTuple_New( 256 );
   for( i = 0; i < 256; i++ )
      PyTuple_SetItem( $result, i, PyLong_FromLong( $1[ i ] ) );
   free( $1 );
}

extern int* frequency( char s[] );
