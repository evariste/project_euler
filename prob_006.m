% The sum of the squares of the first ten natural numbers is, 1^(2) + 2^(2)
% + ... + 10^(2) = 385
% 
% The square of the sum of the first ten natural numbers is, (1 + 2 + ... +
% 10)^(2) = 55^(2) = 3025
% 
% Hence the difference between the sum of the squares of the first ten
% natural numbers and the square of the sum is 3025 ? 385 = 2640.
% 
% Find the difference between the sum of the squares of the first one
% hundred natural numbers and the square of the sum.

% Ans: 25164150

n = 100

% Square of sum
(n * (n+1) / 2)^2

% This last expression is also equal to sum of cubes, i.e.
% 1 + 8 + 27 + . . . + n^3

% Sum of squares
n * (n+1) * (2*n+1) / 6

% Difference
(n * (n+1) / 2)^2 - ( n * (n+1) * (2*n+1) / 6)

% Simplified difference
(n-1) * n * (n+1) * (3*n+2) / 12

