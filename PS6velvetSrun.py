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

usr/bin/time -v velveth fish31/ 31 -fastq -shortPaired $fq_1 $fq_2 -short $fq.unmatched
usr/bin/time -v velvetg fish31 -ins_length 76.79 -exp_cov 60.07

usr/bin/time -v velveth fish41/ 41 -fastq -shortPaired $fq_1 $fq_2 -short $fq.unmatched
usr/bin/time -v velvetg fish41 -ins_length 76.79 -exp_cov 47.23

usr/bin/time -v velveth fish49/ 49 -fastq -shortPaired $fq_1 $fq_2 -short $fq.unmatched
usr/bin/time -v velvetg fish49 -ins_length 76.79 -exp_cov 36.96


usr/bin/tim -v velvetg fish49 -cov_cutoff 20 -ins_length 76.79 -exp_cov 36.96
usr/bin/tim -v velvetg fish49 -cov_cutoff 60 -ins_length 76.79 -exp_cov 36.96
usr/bin/tim -v velvetg fish49 -cov_cutoff auto -ins_length 76.79 -exp_cov 36.96


usr/bin/time velvetg 49 -cov_cutoff auto -min_contig_lgth 500