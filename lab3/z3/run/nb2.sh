#!/bin/bash

#PBS -N nb

#PBS -o nb2.out
#PBS -e nb2.err

#PBS -l walltime=01:00:00

#PBS -l nodes=8:ppn=8

cd /home/parallel/parlab16/lab3/z3

for size in 1024 8192
do
    MT_CONF=0 ./linked_list $size 20 40 40
    MT_CONF=0,1 ./linked_list $size 20 40 40
    MT_CONF=0,1,2,3 ./linked_list $size 20 40 40
    MT_CONF=0,1,2,3,4,5,6,7 ./linked_list $size 20 40 40
    MT_CONF=0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15 ./linked_list $size 20 40 40
    MT_CONF=0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31 ./linked_list $size 20 40 40
    MT_CONF=0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63 ./linked_list $size 20 40 40
done
