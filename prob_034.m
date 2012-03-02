% 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
% 
% Find the sum of all numbers which are equal to the sum of the factorial
% of their digits.
% 
% Note: as 1! = 1 and 2! = 2 are not sums they are not included.
% 
%
% A : 40730 , numbers like 145 are called factorions.

function prob_034

% If number N has d digits then 10^(d-1) <= 10^(d-1) < 10^d

% This sum of the factorials of all its digits cannot exceed d*9!

% Let digits be a_i , i = 1..d
% If 10^(d-1) <= N = sum_i fac(a_i) <= d * 9!
%
% so 10^(d-1) <= d * 9!

% This holds for d = 1, 2 and for a few more values but eventually 10^(d-1)
% which rises exponentially will exceed d*9! which increases linearly.

% So there are a limited set of values of d which the required N can have.

facLookup = factorial([0:9]);

d = 1:10;

a = 10 .^ (d - 1);
b = facLookup(9+1) * d;

maxD = find(a > b, 1, 'first') - 1;
maxVal = 10^maxD - 1;

ss = repmat(' ', 1, 3*maxVal);

% Very slow brute force search. There are only 2 values greater than 2: 145
% and 40585
for i = 10:maxVal
  val = i;
  sumFac = 0;
  while val > 0
    digit = mod(val,10);
    sumFac = sumFac + facLookup(1 + digit);
    val = floor(val / 10);
  end
  
  if (sumFac == i)
    disp(i);
  end
  
    
end


return
