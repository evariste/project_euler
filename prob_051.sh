#!/bin/bash

# By replacing the 1st digit of *3, it turns out that six of the nine
# possible values: 13, 23, 43, 53, 73, and 83, are all prime.

# By replacing the 3rd and 4th digits of 56**3 with the same digit,
# this 5-digit number is the first example having seven primes among
# the ten generated numbers, yielding the family: 56003, 56113, 56333,
# 56443, 56663, 56773, and 56993. Consequently 56003, being the first
# member of this family, is the smallest prime with this property.

# Find the smallest prime which, by replacing part of the number (not
# necessarily adjacent digits) with the same digit, is part of an
# eight prime value family.

# Solution:  121313



#set -e
#set -vx

n=2


# last prime has eight digits in our file.
file=firstMillionPrimes.txt

for i in `seq 0 6`
do
    # pattern for primes with the same digit separated by different amounts.
    patt="\(.\)"
    patt=${patt}`perl -e "print \".\" x $i; chop"`
    patt=$patt"\\1"
    echo $patt
    sed -n -e "/${patt}/ p" $file >> allReps.txt
done

sort -n allReps.txt | uniq > allRepsSort.txt


test -e allRepPatterns.txt && rm allRepPatterns.txt

for p in `cat allRepsSort.txt`
do
    pReduced=$p
    while [[ ${#pReduced} -gt 0 ]]
    do
	d=${pReduced:0:1}
	pMatch=${pReduced//[^$d]/}
	pReduced="${pReduced//${d}/}"
	if [[ ${#pMatch} -gt 1 ]]
	then
	    echo "${p//$d/.}" >> allRepPatterns.txt
	fi

    done

done


for n in `seq 2 8`
do
    let "m = $n + 1"
    sed -n "/^.\{$n\}$/,/^.\{$m\}$/ p" allRepPatterns.txt > temp.txt
    sed -i -e 's/\./x/g' temp.txt
    sed -n "/^.\{$n\}$/,/^.\{$m\}$/ p" firstMillionPrimes.txt > temp2.txt

    for patt in `cat temp.txt`
    do
	patt=`echo $patt | sed -e 's|x|\\\(.\\\)|' -e 's|x|\\\1|g'`
	#echo $patt
	count=`sed -n -e "/^${patt}$/ p" temp2.txt | wc -l`
	if [[ $count -gt 6 ]]; then
	    echo $patt $count
	fi
    done
done

sed -n -e '/^\(.\)2\13\13$/ p' firstMillionPrimes.txt 
121313
222323
323333
424343
525353
626363
828383
929393
