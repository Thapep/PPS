CC = gcc
CFLAGS = -Wall -Wextra -pthread -O0

all: accounts

SRC_FILES= accopt.c /home/parallel/pps/2020-2021/a3/common/aff.c

accounts: $(SRC_FILES) 
	$(CC) $(CFLAGS) $^ -o $@

clean:
	rm -f accounts
