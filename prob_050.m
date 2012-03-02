% The prime 41, can be written as the sum of six consecutive primes: 
%
%     41 = 2 + 3 + 5 + 7 + 11 + 13
% 
% This is the longest sum of consecutive primes that adds to a prime below
% one-hundred.
% 
% The longest sum of consecutive primes below one-thousand that adds to a
% prime, contains 21 terms, and is equal to 953.
% 
% Which prime, below one-million, can be written as the sum of the most
% consecutive primes?
% 
% A:  997651

function prob_050

pList = primes(10^6);

% The sum of p_1, ..., p_547 exceeds 10^6 

% Work our way down from 546

len = 546;

found = false;

while ~found && len > 0
  
  start = 1;
  
  currSum = 0;
  
  while ~found && currSum < 10^6
    currSum = sum(pList(start:start+len-1));
    if any(pList == currSum)
      found = true;
      break;
    end
    start = start + 1;
  end
  
  if currSum >= 10^6
    len = len - 1;
  end
  
end

disp(pList(pList == currSum))
disp('can be written as the sum of')
disp(len)
disp('primes, starting at')
disp(pList(start))

return