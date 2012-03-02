% The prime factors of 13195 are 5, 7, 13 and 29.
% 
% What is the largest prime factor of the number 600851475143 ?
%
% A: 6857

function prob_003


big = 600851475143;

bigStore = big;


[pFacs, inds] = primeFactors(big);

sym(prod(pFacs .^ inds))
sym(big)

pList = primeList(1 + sqrt(big));

isPrime(big)

return



