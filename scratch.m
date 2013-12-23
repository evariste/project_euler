
% Tags : Farey sequence, recursive formula, fractions

%
% Consider the fraction, n/d, where n and d are positive integers. If n<d
% and HCF(n,d)=1, it is called a reduced proper fraction.
%
% If we list the set of reduced proper fractions for d ? 8 in ascending
% order of size, we get:
%
% 1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8,
% 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
%
% It can be seen that there are 3 fractions between 1/3 and 1/2.
%
% How many fractions lie between 1/3 and 1/2 in the sorted set of reduced
% proper fractions for d ? 12,000?

% Ans 7295372


% See recursive formula for next term in Farey Sequence

% http://en.wikipedia.org/wiki/Farey_sequence#Next_term

tic

n = 12000;

a = 0;
b = 1;
c = 1;
d = n;

count = 0;

disp('==========================')

while c < n
  k = floor( (n+b) / d );
  p = k * c - a;
  q = k * d - b;
  
  count = count + 1;

  if c==1 && d==3
    countA = count;
  end
  
  if c==1 && d==2
    countB = count;
    break
  end
  
%   fprintf('== %u : %u/%u ' , count, c, d);
%   if mod(count, 10) == 0
%     fprintf('\n');
%   end

  a = c;
  b = d;
  
  c = p;
  d = q;
  
  
end

fprintf('\n count A, B = %u %u %u \n' , countA, countB , countB-countA-1);

%  count A, B = 14590756 21886129 7295372 

disp('==========================')
toc

