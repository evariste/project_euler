% A Pythagorean triplet is a set of three natural numbers, a < b < c, for
% which, a^(2) + b^(2) = c^(2)
% 
% For example, 3^(2) + 4^(2) = 9 + 16 = 25 = 5^(2).
% 
% There exists exactly one Pythagorean triplet for which a + b + c = 1000.
% Find the product abc.

% Ans: 31875000

% Pythag triple (a,b,c) can be written
%
% a = m^2 - n ^2   b = 2mn    c = m^2 - n^2  with m > n > 0
%
% a + b + c = 1000 can be re-written as
%
% m (m + n) = 500  after simplification.
%
% I.e. we can search over factors of 500 and find m and n that fit.

facs = factors(500);
facs = sort(facs);

for i = 1:numel(facs)
  m = facs(i);
  n = ( 500 / m ) - m ;

  if m < n || n < 0
    continue
  end

  a = m^2 - n^2;
  b = 2*m*n;
  c = m^2 + n^2;
  
  disp([m n a  b  c a+b+c c^2-a^2-b^2 ]);
  fprintf('Answer: ')
  disp(sym([a b c a*b*c]))
end

% Only one row has a, b and c all positive: 
% a=375    b=200     c=425


