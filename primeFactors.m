%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
function [pFacs, inds] = primeFactors(n)
% Return row vectors
%
%   p_1 p_2 ..., p_k
%
% prime factors of n and corresponding indices 
%
%   d_1, d_2, ..., d_k 
%
% i.e. 
% 
%  n = p_1^d_1 p_2^d_2 .... p_k^d_k
%

if  n ~= round(n)
  error('primeFactors: n must be integer');
end

if n < 0
  n = -n;
end

% Allow up to 1000 prime factors for now
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
  end
  
  pFacs(i) = pFac;
  inds(i)  = ind;
  i = i + 1;
end

pFacs = pFacs(1:i-1).';
inds  = inds(1:i-1).';

return
