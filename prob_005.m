% 
% 2520 is the smallest number that can be divided by each of the numbers
% from 1 to 10 without any remainder.
% 
% What is the smallest positive number that is evenly divisible by all of
% the numbers from 1 to 20?

% Ans: 232792560


maxFactor = 20;

% The number we seek needs to divide all the primes less than or equal to
% the largest factor.
plist = primeList(maxFactor);

% The index of each prime needs to be as large as possible without
% exceeding the maximum factor.
inds = floor( ones(size(plist)) * log(maxFactor) ./ log(plist) );

n = prod(plist .^ inds)

for i = 1:maxFactor
  disp(sym([i n/i]))
end

% Alternatively
n = 1;
for i = 2:maxFactor
  n = lcm(n, i);
end
disp(n)


