import sys

sys.path.append('/home/andr/work/jpy/build/lib.linux-x86_64-3.5')

import jpy
import jpyutil

jpyutil.init_jvm(jvm_maxmem='512M', jvm_classpath=['/home/andr/work/jpy/testClasses'])

FileInputStream = jpy.get_type('java.io.FileInputStream')
InputStreamReader = jpy.get_type('java.io.InputStreamReader')
BufferedReader = jpy.get_type('java.io.BufferedReader')
File = jpy.get_type('java.io.File')
FileReader = jpy.get_type('java.io.FileReader')
String = jpy.get_type('java.lang.String')
System = jpy.get_type('java.lang.System')


f = File('test_java.txt')

fin = BufferedReader(FileReader(f))

for i in range(4):
    stringLine = String(fin.readLine())
    System.out.println(stringLine)

