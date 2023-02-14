#!/bin/bash
for ((i=1;i<=32;i=i*2))
do
	export OMP_NUM_THREADS=${i}
	for ((j=1;j<=32;j++))
	do
		export TF_INTRA_OP_PARALLELISM_THREADS=${j}
		for ((k=1;k<=32;k*=2))
		do
			export TF_INTER_OP_PARALLELISM_THREADS=${k}
			rm ${i}_${j}_${k}.log
			dp train input.json -l ${i}_${j}_${k}.log
			echo "OMP_NUM_THREADS=${OMP_NUM_THREADS}, INTRA=${TF_INTRA_OP_PARALLELISM_THREADS}, INTER=${TF_INTER_OP_PARALLELISM_THREADS}"
		done
	done
done
