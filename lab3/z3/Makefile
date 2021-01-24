CC = gcc
CFLAGS = -Wall -Wextra -pthread

## Remove some warnings.
CFLAGS += -Wno-unused-parameter -Wno-unused-variable -Wno-unused-function

RES=-DPRINT_RESULTS

all: linked_list

## Which linked list implementation to use?
LL_FILE = lazy.c

## Additional source files
SRC_FILES = /home/parallel/pps/2020-2021/a3/common/aff.c

linked_list: main.c ${LL_FILE} ${SRC_FILES}
	$(CC) $(CFLAGS) $^ -o $@

clean:
	rm -f linked_list
