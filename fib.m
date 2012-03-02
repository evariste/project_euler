function val = fib(n)
% nth term of fibonacci sequence.
% n can be an array in which case an array is returned.

phi = 0.5 * (1 + sqrt(5));

val = floor(0.5 + phi.^n / sqrt(5));

