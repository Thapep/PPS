#!/bin/bash

#PBS -N z2

#PBS -o make.out
#PBS -e make.err

#PBS -l walltime=00:01:00

#PBS -l nodes=1

cd /home/parallel/parlab16/lab3/z2
make
