function i = factoradic2index(f)
% Return the index of a factoradic number that locates the corresponding
% permutation of n elements in the set of all permutations that have been
% lexicographically ordered.  The number of elements n is the length of the
% input array f representing the factoradic number.

n = numel(f);

fac = 1;
count = 1;

i = 0;

for k = n-1:-1:1
  i = i + fac * f(k);
  count = count + 1;
  fac = fac * count;
end



return