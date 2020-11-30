#!/bin/bash

#PBS -N redblack

#PBS -o make.out
#PBS -e make.err

#PBS -l nodes=1:ppn=1

#PBS -l walltime=00:01:00

cd /home/parallel/parlab16/lab2/gauss/serial
make
