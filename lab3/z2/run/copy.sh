#/bin/bash
## :%s/foo/bar/g replace foo with bar in all lines

sed -n '1,14p' array_lock.out > array_lock16.out
sed -n '15,28p' array_lock.out > array_lock1024.out
sed -n '29,42p' array_lock.out > array_lock8192.out


