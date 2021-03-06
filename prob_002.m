% Each new term in the Fibonacci sequence is generated by adding the
% previous two terms. By starting with 1 and 2, the first 10 terms will be:
% 
% 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
% 
% Find the sum of all the even-valued terms in the sequence which do not
% exceed four million.
%
%
% A: 4613732


% Use these indices for the sequence to match those used by, e.g. Wikipedia
% index: 0 1 2 3 4 5 6  7  8  9 10 
% value: 0 1 1 2 3 5 8 13 21 34 55 
%
% Starting at n=1, matlab style, sequence begins with odd odd (1, 1) so
% must be:   o o e o o e o o e ...


maxVal = 4e06;

% Using helper functions:
n = i_fib(maxVal);
if fib(n) > maxVal
  n = n -1;
end
f = fib(1:n);
sum(f(3:3:end))


% Brute force approach.
a = zeros(1,100);

a(1) = 1;
a(2) = 1;

for i = 3:100
  a(i) = a(i-1) + a(i-2);
end

% a(33) < 4 million < a(34)
a = a(a < maxVal);
sum(a(3:3:end))


% Another way:

% Use the relation:
% F_3n = 5 F_n^3 + 3 (-1)^n F_n
lastInd = numel(a);
F = zeros(1, lastInd);
sum = 0;

for i = 1:floor(lastInd/3)
  if (i < 3)
    F(i) = 1;
  else
    F(i) = F(i-1) + F(i-2);
  end

  F_3i = 5 * F(i)^3 + 3 * (-1)^i * F(i);
  sum = sum + F_3i;
  fprintf('%d %d \n', F_3i, sum);
end



