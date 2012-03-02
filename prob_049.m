% The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
% increases by 3330, is unusual in two ways: (i) each of the three terms
% are prime, and, (ii) each of the 4-digit numbers are permutations of one
% another.
% 
% There are no arithmetic sequences made up of three 1-, 2-, or 3-digit
% primes, exhibiting this property, but there is one other 4-digit
% increasing sequence.
% 
% What 12-digit number do you form by concatenating the three terms in this
% sequence?

% A : 296962999629


function prob_049


pList = primes(10000);

pList = pList(pList > 999);

for n = 1:numel(pList)
  p1 = pList(n);
  
  % Find all permutations of current prime
  digsP1 = str2num(num2str(p1)')';
  permsDigsP1 = perms(digsP1);
  permsDigsP1 = permsDigsP1 * [1000 100 10 1]';

  % Find which permutations are primes between 1000 and 10000
  currSet = zeros(24, 1);
  currSet(1) = p1;
  ind = 2;
  for i = 1:numel(permsDigsP1)
    p2 = permsDigsP1(i);
    if ~any(pList == p2)
      continue;
    end
    if any(currSet == p2)
      continue;
    end
    currSet(ind) = p2;
    ind = ind + 1;
    
  end
  
  % Do we have at least three primes that are permutations of each other?
  if ind < 3
    continue
  end
  
  % Check if the current set (which may have more than three primes)
  % contains a subset of three that are in arithmetic sequence.
  currSet = currSet(currSet>0);
  possibleSeqs = nchoosek(currSet, 3);
  for i = 1:size(possibleSeqs, 1)
    abc = sort(possibleSeqs(i, :));
    % b - a = c - b
    % c - 2 b + a = 0
    if abc * [1 -2 1]' == 0
      disp(abc)
      disp(sym(abc * [10^8 10^4 1]'));
    end
  end
end

return

