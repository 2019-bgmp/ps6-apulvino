#!/bin/bash


#SBATCH --partition=bgmp        
#SBATCH --job-name=VelvetSrun     
#SBATCH --output=VelvetSrun.out         
#SBATCH --error=VelvetSrun.err        
#SBATCH --time=0-01:00:00       
#SBATCH --nodes=1               
#SBATCH --ntasks-per-node=1     
#SBATCH --account=bgmp      


file1=/projects/bgmp/shared/Bi621/800_3_PE5_interleaved.fq_1
file2=/projects/bgmp/shared/Bi621/800_3_PE5_interleaved.fq_2
file3=/projects/bgmp/shared/Bi621/800_3_PE5_interleaved.fq.unmatched

/usr/bin/time -v velveth fish31/ 31 -fastq -shortPaired $file1 $file2 -short $file3
/usr/bin/time -v velvetg fish31 -ins_length 76.79 -exp_cov 60.07