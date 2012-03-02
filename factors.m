function facs = factors(n)
% Return all factors of n

if n < 1
  facs = [];
  return;
end

[pFacs, ind] = primeFactors(n);

% Get all combinations of indices
indPlusOne = ind + 1;

nFacs = prod(indPlusOne);

facs = zeros(1, nFacs);

for i = 1:nFacs
  currInds = ind2sub_pa(indPlusOne, i) - 1;
  facs(i) = prod(pFacs .^ currInds);
end

return