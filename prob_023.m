
% A perfect number is a number for which the sum of its proper divisors is
% exactly equal to the number. For example, the sum of the proper divisors
% of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect
% number.
% 
% A number n is called deficient if the sum of its proper divisors is less
% than n and it is called abundant if this sum exceeds n.
% 
% As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the
% smallest number that can be written as the sum of two abundant numbers is
% 24. By mathematical analysis, it can be shown that all integers greater
% than 28123 can be written as the sum of two abundant numbers. However,
% this upper limit cannot be reduced any further by analysis even though it
% is known that the greatest number that cannot be expressed as the sum of
% two abundant numbers is less than this limit.
% 
% Find the sum of all the positive integers which cannot be written as the
% sum of two abundant numbers.
% 
% A: 4179871


function prob_023

maxVal = 28123;

checked = zeros(1, maxVal);

% for i = 1:maxVal
%   
%   if checked(i)
%     continue;
%   end
%   
%   if abundant(i)
%     checked(i:i:maxVal) = 1;
%   end
%   
% end
% 
% abundNos = 1:maxVal;
% abundNos = abundNos(checked > 0);

% save('abundNos.mat', 'abundNos');
load abundNos

% Which numbers are reachable as the sum of two abundant numbers.
reachable = zeros(maxVal, 1);

limit = maxVal + 1;

for i = 1:numel(abundNos)
  a = abundNos + abundNos(i);
  a = a(a < limit);
  reachable(a) = 1;
end

unreachable = 1:maxVal;
unreachable = unreachable(~reachable);

sum(unreachable)

return

function abundant = abundant(n)

abundant = 0;

[pFacs, inds] = primeFactors(n);

% Numbers of form p^k are deficient.
if numel(pFacs) == 1
  return
end

% See sumFactors.m
total = 1;
for k = 1:numel(pFacs)
  total = total * (pFacs(k)^(inds(k)+1) - 1) / (pFacs(k) - 1);
end

if (total > 2*n)
  abundant = 1;
end

return
