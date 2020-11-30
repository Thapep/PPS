#!/bin/bash

## Give the Job a name
#PBS -N make_omp_gol

## Outupt, error files
#PBS -o make.out
#PBS -e make.err

## Run time
#PBS -l walltime=00:10:00

## Number of machines
#PBS -l nodes=1:ppn=1

cd /home/parallel/parlab16/lab1/fw/parallel
make
