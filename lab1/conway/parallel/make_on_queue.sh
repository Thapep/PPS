#!/bin/bash

## Give the Job a name
#PBS -N make_omp_gol

## Outupt, error files
#PBS -o mgol.out
#PBS -e mgol.err

## Run time
#PBS -l walltime=00:01:00

## Number of machines
#PBS -l nodes=1

module load openmp
cd /home/parallel/parlab16/a1/conway/parallel
make
