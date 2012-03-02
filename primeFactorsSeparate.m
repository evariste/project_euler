%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
function pFacs = primeFactorsSeparate(n)
% Return a list of prime factors pFacs where primes are repeated according
% to their index in the factorisation of n.
% i.e. pFacs = [p_1 p_1 ... p_2 p_2 ... p_k]


if  n ~= round(n)
  error('primeFactorsSeparate: n must be integer');
end

if n < 0
  n = -n;
end

% Allow up to 1000 prime factors
MAX_FACTORS = 1000;
pFacs = zeros(MAX_FACTORS, 1);
inds  = zeros(MAX_FACTORS, 1);
i = 1;

while n > 1 && i <= MAX_FACTORS
  pFac = getPrimeFactor(n);

  ind = 0;
  while mod(n, pFac) == 0
    n = n / pFac;
    ind = ind + 1;
    pFacs(i) = pFac;
    i = i + 1;
  end
  
end

if (i > MAX_FACTORS)
  error('primeFactorsSeparate: Maximum number of factors exceeded');
end

pFacs = pFacs(1:i-1)';

return
