%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
function newList = growPrimeList(oldList)
% Increment an ordered list of primes.
% Argument oldList must be a complete list of primes up to the nth, i.e. 
%    [2, 3, 5, ..., p_n]
% return newList which is [ oldList p_n+1 ]

% should be able to grow this list much further than by just one element!



newList = oldList;

if oldList == 2
  newList = [2 3];
  return
end

currCand = oldList(end) + 2;

currIsPrime = false;
while ~currIsPrime
  i = 1;
  currIsPrime = true;
  
  while oldList(i) <= sqrt(currCand)
    if mod(currCand, oldList(i)) == 0
      currIsPrime = false;
      currCand = currCand + 2;
      break;
    end
    i = i + 1;
  end
  
end

newList = [oldList currCand];

return
