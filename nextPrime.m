%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
function nextprime = nextPrime(val)
% Give the next prime greater than val.
% SLOW!

if val == 2
  nextprime = 3;
  return
end

currCand = val + 1 + mod(val, 2);

currIsPrime = false;
while ~currIsPrime
  i = 2;
  currIsPrime = true;
  
  while i <= sqrt(currCand)
    if mod(currCand, i) == 0
      currIsPrime = false;
      currCand = currCand + 2;
      break;
    end
    i = i + 1;
  end
  
end

nextprime = currCand;

return
