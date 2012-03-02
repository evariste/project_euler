function n = i_fib(x)
% seek n s.t.
% fib(n-1) < x <= fib(n)

phi = 0.5 * (1 + sqrt(5));

% Use approximation in fib(n)
%
% x = phi^alpha / sqrt(5)
%
% alpha helps us find n

alpha = log(x * sqrt(5)) / log(phi);

n = 1 + floor(alpha);

if fib(n-1) == x
  n = n - 1;
end

return