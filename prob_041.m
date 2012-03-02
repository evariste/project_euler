% We shall say that an n-digit number is pandigital if it makes use of all
% the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital
% and is also prime.
% 
% What is the largest n-digit pandigital prime that exists?
% 
% A: 7652413
%


function prob_041

% sum(1:8) = 36 and sum(1:9) = 45 so we cannot have 8- or 9-digit
% pandigital primes.

% So lets start with a reverse search of 7-digit pandigital numbers and
% test each for primality.

% Leading digit is always seven.

% allowable units digits
units = [3 1];

% Digits between the leading and the units.
digs = [2 4 5 6];


% decimal multiplier vector
dec = ones(numel([digs units]), 1);
for i = 2:numel(dec)
  dec(i) = 10 * dec(i-1);
end
dec = flipud(dec);

  
 for i = 1:numel(units)
   % current unit
   u = units(i);
   % The unused units
   uu = setdiff(units, u);
   % All perms for the 'between' digits
   rest = perms([digs uu]);
   % Paste in the unit
   rest = [rest u*ones(size(rest,1), 1)];
   
   rest = sort(rest * dec, 'descend');
  
   n = 10;
   j = 1;
   while ~isprime(n) && j < numel(rest)
     n = 7000000 + rest(j);
     j = j + 1;
   end
   
   if (isprime(n))
     disp(n);
     return;
   end
  
  
end

