% The decimal number, 585 = 1001001001_(2) (binary), is palindromic in both
% bases.
% 
% Find the sum of all numbers, less than one million, which are palindromic
% in base 10 and base 2.
% 
% (Please note that the palindromic number, in either base, may not include
% leading zeros.)

% A : 872187

function prob_036

total = 0;

% Enumerate palindromes base 10, less than a million
for d = 1:3
  fst  = 10^(d-1);
  last = 10^d;

  % odd sized palindromes with 2d-1 digits
  for n = fst:last-1
    pal  = n * fst + flip(floor(n/10));
    % Can only be a binary palindrome if it is odd.
    if mod(pal,2) == 0
      continue
    end
    flipBase2 = flip(pal, 2);
    if strcmp(dec2bin(pal), dec2bin(flipBase2))
      fprintf('%d %s\n', pal, dec2bin(pal))
      total = total + pal;
    end
  end
  % even sized with 2d digits
  for n = fst:last-1
    pal = n * last + flip(n);
    if mod(pal,2) == 0
      continue
    end
    flipBase2 = flip(pal, 2);
    if strcmp(dec2bin(pal), dec2bin(flipBase2))
      fprintf('%d %s\n', pal, dec2bin(pal))
      total = total + pal;
    end
    
  end
end

disp(total)

return

function flipped = flip(n, base)
% Pre: n >= 0;
if n == 0
  flipped = 0;
  return
end

if (nargin < 2)
  base = 10;
end

% Can handle up to 1000 digits.
digits = zeros(1000,1);
count = 0;

while n > 0
  count = count + 1;
  digits(count) = mod(n, base);
  n = floor(n / base);
end

digits = digits(1:count);

flipped = digits(1);
for i = 2:count
  flipped = base * flipped + digits(i);
end


return
