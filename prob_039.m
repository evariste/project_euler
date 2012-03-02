function prob_039


maxP = 1000;

% 1000 >= 2m^2 + 2mn
% 500 >= m^2 + mn
% 500 >= m(m + n)
% 500 >= m k where k = m+n

row = 0;
cache = zeros(1000, 3);

for m = 1:(maxP/2)
  maxK = 1 + floor(maxP / 2 / m);
  
  for k = 1:maxK
    n = k - m;
    if (n < 1 || m <= n || gcd(m,n) > 1)
      continue;
    end

    a = m^2 - n^2;
    b = 2*m*n;
    c = m^2 + n^2;
    p = a + b + c;
    
    j = 1;
    ja = a;
    jb = b;
    jc = c;
    while p <= maxP
    
      row = row + 1;
      cache(row, :) = sort([ja jb jc]);
      j = j + 1;
      ja = j * a;
      jb = j * b;
      jc = j * c;
      p = ja + jb + jc;
    end
    
  end
end
cache = cache(1:row,:);
cache = unique(cache, 'rows');
ps = sum(cache,2);
x = 1:max(ps);
hist(ps, x);
binCounts = hist(ps, x);
[m, i] = max(binCounts);
inds = ps==i;

disp([cache(inds, :) ps(inds)])