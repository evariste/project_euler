function nFacs = numberOfDivisors(n)

if n == 0
  nFacs = 0;
  return
end

if n < 0
  n = -1 * n;
end

if n == 1
  nFacs = 1;
  return;
end

[~, ind] = primeFactors(n);

% Get all combinations of indices
indPlusOne = ind + 1;

nFacs = prod(indPlusOne);

return
