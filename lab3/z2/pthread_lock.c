#include "lock.h"
#include "/home/parallel/pps/2020-2021/a3/common/alloc.h"
#include <pthread.h>

struct lock_struct {
	pthread_spinlock_t lock;
};

lock_t *lock_init(int nthreads)
{
	lock_t *lock;

	XMALLOC(lock, 1);
	/* other initializations here. */
	pthread_spin_init(&lock->lock,PTHREAD_PROCESS_SHARED);
	return lock;
}

void lock_free(lock_t *lock)
{
	XFREE(lock);
	//pthread_spin_destroy(&lock->lock);
}

void lock_acquire(lock_t *lock)
{
	pthread_spin_lock(&lock->lock);
}

void lock_release(lock_t *lock)
{
	pthread_spin_unlock(&lock->lock);
}

