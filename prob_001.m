% If we list all the natural numbers below 10 that are multiples of 3 or 5,
% we get 3, 5, 6 and 9. The sum of these multiples is 23.
% 
% Find the sum of all the multiples of 3 or 5 below 1000.

clear

max = 1000;
a = 3;
b = 5;

upper = max-1;

n = 1:upper;


ma = mod(n, a) == 0;
mb = mod(n, b) == 0;

maOrb = ma | mb;


% Number of multiples of 3 or 5
numel(find(maOrb))

% How many multiples of each
countA = floor(upper/a);
countB = floor(upper/b);
% How many multiples of both a and b?
countAB = floor(upper/lcm(a,b));

% Number of multiples of 3 or 5
countAorB = countA + countB - countAB


sumA = a * countA*(countA+1)/2 + b * countB*(countB+1)/2 - a * b * countAB*(countAB+1)/2




