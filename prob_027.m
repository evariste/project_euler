function prob_027

% Euler published the remarkable quadratic formula:
% 
% n² + n + 41
% 
% It turns out that the formula will produce 40 primes for the consecutive
% values n = 0 to 39. However, when n = 40, 40^(2) + 40 + 41 = 40(40 + 1) +
% 41 is divisible by 41, and certainly when n = 41, 41² + 41 + 41 is
% clearly divisible by 41.
% 
% Using computers, the incredible formula  n² ? 79n + 1601 was discovered,
% which produces 80 primes for the consecutive values n = 0 to 79. The
% product of the coefficients, ?79 and 1601, is ?126479.
% 
% Considering quadratics of the form:
% 
%     n² + an + b, where |a| < 1000 and |b| < 1000
% 
%     where |n| is the modulus/absolute value of n e.g. |11| = 11 and |?4|
%     = 4
% 
% Find the product of the coefficients, a and b, for the quadratic
% expression that produces the maximum number of primes for consecutive
% values of n, starting with n = 0.
% 
% A: -61*971 = -59231

% First 10000 primes.
plist = primes(104729 + 1);

bList = primes(1000);
bList = [-1*fliplr(bList) bList];


maxP = plist(end);
maxSize = 999;

longestList = 0;
bestA = 0;
bestB = 0;

for a = -maxSize:maxSize
  
  for i = 1:numel(bList)
    b = bList(i);
    
    
    n = 0;
    val = b;
    count = 1;
    
    while val < 0
      n = n + 1;
      val = n*n + a*n + b;
    end
    
    while ismember(val, plist)
      n = n+1;
      val = n*n + a*n + b;
      count = count + 1;
    end
    
    if count > longestList
      bestA = a;
      bestB = b;
      longestList = count;
      fprintf('%d  %d  %d \n', a, b, count);
    end
    
  end
end
% 
% -999  -997  2 
% -999  -983  3 
% -999  -953  4 
% -999  -89  6 
% -997  -937  13 
% -887  -541  15 
% -413  -97  16 
% -61  971  72 



return
