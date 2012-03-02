%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
function pList = primeList(maxVal)
% Use sieve of Eratosthenes to get a list of primes up to a limiting value.

pList = 1:maxVal;

inds = true(size(pList));

% 1 is not a prime.
inds(1) = 0;

i = 1;
while i <= sqrt(maxVal)
  while i <= maxVal && ~inds(i)
    i = i + 1;
  end
  currPrime = i;
  i = i + 1;
  inds(2*currPrime:currPrime:end) = 0;  
end

pList = pList(inds);

return
