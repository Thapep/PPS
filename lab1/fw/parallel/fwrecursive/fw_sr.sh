#Give  the Job a name
#PBS -N run_fw_sr

## Outupt, error files
#PBS -o fw_sr1.out
#PBS -e fw_sr1.err

## Run time
#PBS -l walltime=00:30:00

## Number of machines
##PBS -l nodes=1:ppn=1

module load openmp
cd /home/parallel/parlab16/lab1/fw/parallel

for thr in 1 2 4 6 8 16 32 64 
do
  echo 'threads:' $thr
  for N in 1024 2048 4096 
  do	
    export OMP_NUM_THREADS=$thr
    for b in 64 128 256
    do
      ./fw_sr $N $b
    done
  done
done
