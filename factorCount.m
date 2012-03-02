function noOfFacs = factorCount(n)
% How many factors does n have?

[~, ind] = primeFactors(n);

noOfFacs = prod(1 + ind);

return