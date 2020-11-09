#!/bin/bash

##Job name
#PBS -N run_omp_gol

## Out, error files
#PBS -o rgol.out
#PBS -e rgol.err

##Number of machines
#PBS -l nodes=1:ppn=8

##Run time
#PBS -l walltime=00:10:00

cd /home/parallel/parlab16/a1/conway/serial
./omp_gol 64 1000
./omp_gol 1024 1000
./omp_gol 4096 1000
