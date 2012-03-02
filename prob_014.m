function prob_014

% The following iterative sequence is defined for the set of positive
% integers:
% 
% n ? n/2 (n is even) n ? 3n + 1 (n is odd)
% 
% Using the rule above and starting with 13, we generate the following
% sequence: 13 ? 40 ? 20 ? 10 ? 5 ? 16 ? 8 ? 4 ? 2 ? 1
% 
% It can be seen that this sequence (starting at 13 and finishing at 1)
% contains 10 terms. Although it has not been proved yet (Collatz Problem),
% it is thought that all starting numbers finish at 1.
% 
% Which starting number, under one million, produces the longest chain?
% 
% NOTE: Once the chain starts the terms are allowed to go above one
% million.

% Ans: 837799  (524 steps to reach 1)


clear
tic

maxToCheck = 1000000;
maxVal = maxToCheck + 1;
visited = zeros(maxToCheck, 1);

maxLen = 0;
maxStarter = 1;

for i = 2:maxToCheck
  
  % No need to visit a number that was part of an earlier chain, its hops
  % to one will be fewer than the current max.
  if ~visited(i)
    [len_i, visited] = chainLength(i, visited, maxVal);
  end
  
  if maxLen < len_i
    maxLen = len_i;
    maxStarter = i;
  end
  
end


toc

fprintf('%d  %d \n', maxStarter, maxLen);

return

function [len, visited] = chainLength(n, visited, maxVal)
% No of steps to reach 1
% Pre: n >= 1

len = 0;
curr = n;

while curr > 1
  
  currOver2 = curr / 2;
  
  if floor(currOver2) == currOver2
    curr = curr / 2;
  else
    curr = 3 * curr + 1;
  end
  len = len + 1;
  
  % Keep track of what has been visited.
  if curr < maxVal
    visited(curr) = 1;
  end
  
end

return
