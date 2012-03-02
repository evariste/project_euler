% The first two consecutive numbers to have two distinct prime factors are:
% 
% 14 = 2 × 7 
% 15 = 3 × 5
% 
% The first three consecutive numbers to have three distinct prime factors
% are:
% 
% 644 = 2² × 7 × 23 
% 645 = 3 × 5 × 43 
% 646 = 2 × 17 × 19.
% 
% Find the first four consecutive integers to have four distinct primes
% factors. What is the first of these numbers?

% A:  134043 134044 134045 134046


i = 1;

nReq = 4;

while true
  i = i + 1;
  
  if numel(primeFactors(i)) < nReq
    continue;
  end
  
  found = 1;
  for j = 1:nReq-1

    if numel(primeFactors(i + j)) < nReq
      found = 0;
      break;
    end
    
  end
  
  if ~found
    continue;
  end
  
  break;
end

disp( (i:i+nReq-1));


for j = 0:nReq-1
  disp(i + j)
  disp(primeFactors(i + j))
  disp('')
end
% 
%       134043
% 
%      3     7    13   491
% 
%       134044
% 
%      2    23    31    47
% 
%       134045
% 
%      5    17    19    83
% 
%       134046
% 
%      2     3    11   677
