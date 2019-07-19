#!/anaconda3/bin/python

import argparse
import re

def get_args():
	parser = argparse.ArgumentParser(description="k_mer coverage file for 5x and 10x coverage")
	parser.add_argument("-f", "--file", help="the fastq file, contigs.fa", required=True)
	parser.add_argument("-k", "--k_cov_lim", help="k-mer coverage limit", required=True)
	return parser.parse_args()
	
args = get_args()
file = args.file
k = int(args.k_cov_lim)

k_mer_length = []
k_cov_array = []
max_k_length = []
coverage = []
bins = {}


with open(file, "r") as fh:
	contig_count = 0
	while True:
		
		line = fh.readline()
		if line == "":
			# EOF = end of file
			break
	
		if ">" == line[0]:
			contig_count += 1	
			#print(line)
			
		
		
			x = 48
			k_len_contig = int(re.findall(r'length_(\d+)_cov_.*', line)[0])	#extracts k-mer length of each contig	
			k_mer_length.append(k_len_contig + x)							#appends k length to dictionary 
											
			k_cov = float(re.findall(r'length_\d+_cov_(.*)', line)[0])		# same thing but for kmer coverage
			k_cov_array.append(k_cov)										#appends to the dictionary but for kmer coverage
			
	
	mean_kmer_len = sum(k_mer_length)/len(k_mer_length)						#mean kmer length
	
	total_assembly_length = sum(k_mer_length)								#sums all nucleotides of all contigs in file
	
	mean_depth_cov = sum(k_cov_array) / len(k_cov_array)


	LN = 0		
	k_mer_length.sort(reverse=True)	
	#print(k_mer_length)
	total_sum = 0											#generates the N50 values with running total LN; k_mer_length[LN] is value at the position = N50
	while total_sum < (total_assembly_length / 2):
		total_sum += k_mer_length[LN]
		
		if total_sum >= total_assembly_length / 2:
			N50 = k_mer_length[LN]
		LN += 1
		
	
	

		
	for element in sorted(k_mer_length): 
		x = element // 100 * 100
		if x in bins:
			bins[x]+= 1			#accessing bin
			#key bins at x (x=number of bin 0,100,200,300, etc.); values= # of items in bins
		else:
			upd={x:1}
			bins.update(upd)			#adds bin to bin if bin not currently existing
	
	print("# Contig Length","Number Contigs in Bin")			
	for x in bins:
		print(x, "\t", bins[x])	
		#key is x (values of x are the bins) value is bins[x] (values of bins[x] are numbers of reads with length less than given value (ex. bin 200 incl 199 to 100))		
	
	print("N50 of Assembly:", N50)
	
	print("Mean Depth of Coverage:", mean_depth_cov)
	
	print("Total Assembly Length:", total_assembly_length)

	print("Mean Contig Length:", mean_kmer_len)
			
	print("Maximum Contig Length:", sorted(k_mer_length)[-1])	
	#print(sorted(k_cov_array))													
																					
		#k_mer_length.append(k_len_contig)
			#print(k_mer_length)
			
	print("Number of contigs:", contig_count)