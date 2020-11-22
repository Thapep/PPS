#Give the Job a name
#PBS -N fwrserial

## Outupt, error files
#PBS -o fwr.out
#PBS -e fwr.err

## Run time
#PBS -l walltime=00:30:00

## Number of machines
#PBS -l nodes=1:ppn=1

cd /home/parallel/parlab16/lab1/fw/serial

for N in 1024 2048 4096
do
  for b in 64 128 256
  do	
    ./fw_sr $N $b
  done
done
