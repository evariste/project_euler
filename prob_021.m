% 
% Let d(n) be defined as the sum of proper divisors of n (numbers less than
% n which divide evenly into n). If d(a) = b and d(b) = a, where a ? b,
% then a and b are an amicable pair and each of a and b are called amicable
% numbers.
% 
% For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22,
% 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1,
% 2, 4, 71 and 142; so d(284) = 220.
% 
% Evaluate the sum of all the amicable numbers under 10000.

% A: 31626

function prob_021

maxVal = 10000;

visited = zeros(1,maxVal);

total = 0;

for i = 2:maxVal
  if visited(i)
    continue;
  end
  visited(i) = 1;
  
  d_i = sumFactors(i) - i;
  
  % Careful, an amicable number may have a partner larger than maxVal.
  if (d_i <= maxVal && visited(d_i))
    continue;
  end
  
  if (d_i <= maxVal)
    visited(d_i) = 1;
  end
  
  if i == (sumFactors(d_i) - d_i) && i ~= d_i
    total = total + i + d_i;
    fprintf('%d %d\n' , i, d_i);
  end
end

fprintf('Total : %d\n' , total);

return

