#!/usr/bin/env bash

for i in data/*gz
do
	nf=$(echo $i | cut -d '.' -f 1 | cut -d '/' -f 2)
	dip-c/dip-c bincon -b 1000000 -H -l dip-c/color/hg19.chr.len $i > result/whole_genome/1mb/${nf}.bincon.txt 
	dip-c/dip-c bincon -i -b 1000000 -H -l dip-c/color/hg19.chr.len . > result/whole_genome/1mb/${nf}.bincon.info


done 
