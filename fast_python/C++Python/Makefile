CC = c++
CPLUS_INCLUDE_PATH=/usr/include/python2.7
PYLIBPATH = $(shell python-config)/lib
LIB = -L$(PYLIBPATH) $(shell python-config) -lboost_python
OPTS = $(shell python-config) -O2



default: zoo.so
	@python ./visit_zoo.py

zoo.so: zoo.o
	$(CC) $(LIB) -Wl,-rpath,$(PYLIBPATH) -shared $< -o $@

zoo.o: zoo.cpp Makefile
	$(CC) $(OPTS) -c $< -o $@

clean:
	rm -rf *.so *.o

.PHONY: default clean
