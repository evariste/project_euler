function digits = index2factoradic(ind, n)
% Find factoradic representation of decimal number ind which indexes the
% permutations of n elements. The permutatons are lexicographically ordered
% and their indices start at zero.
%
% The elements that are permuted are assumed to be '1', '2', . . ., 'n'
%

f = factorial(n-1);

if ind > n*f - 1 || ind < 0
  error('index2factoradic: no such index');
end

digits = zeros(1,n);

k = 1;
while ind > 0
  digits(k) = floor(ind / f);
  ind = rem(ind, f);
  f = f / (n - k);
  k = k + 1;
end

return

