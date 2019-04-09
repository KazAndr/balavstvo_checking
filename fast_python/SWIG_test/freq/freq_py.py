#!/usr/bin/python
# -*- coding: utf-8 -*-

from sys import argv
import freq

sarg = lambda : ( len( argv ) > 1 and argv[ 1 ] ) or str( input( "string?: " ) )

f = freq.frequency( sarg() )

s = ""
for i in range( 256 ):
    if f[ i ] != 0:
        s = s + "'%c'[0x%x]:%d " % ( i, i, f[ i ] )

print(s)
