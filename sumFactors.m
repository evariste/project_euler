function total = sumFactors(n)
% Sum of all factors of n, including n.
%
% if n = p_1^i_1 * p_2^i_2 * . . . * p_n^i_n
%
% sum of factors is
%
% prod_{k=1}^{n} (1+p_k+ ... p_k^i_k)
%
% = prod_{k=1}^{n} (p_k^(i_k+1) - 1) / (p_k - 1)
%

[pFacs, inds] = primeFactors(n);

total = 1;
for k = 1:numel(pFacs)
  total = total * (pFacs(k)^(inds(k)+1) - 1) / (pFacs(k) - 1);
end

% Following line is probably less efficient.
% total = sum(factors(n));

return