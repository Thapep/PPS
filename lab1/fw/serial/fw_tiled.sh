#Give the Job a name
#PBS -N fwtserial

## Outupt, error files
#PBS -o fwt.out
#PBS -e fwt.err

## Run time
#PBS -l walltime=00:30:00

## Number of machines
#PBS -l nodes=1:ppn=1

cd /home/parallel/parlab16/lab1/fw/serial

for N in 1024 2048 4096
do
  for b in 16 32 64 128 256
  do
    ./fw_tiled $N $b
  done
done
