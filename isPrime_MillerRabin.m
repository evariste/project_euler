function isPrime = isPrime_MillerRabin(n)
% Use Miller-Rabin primality test.  Only definite up to a limit.

% deal with particular cases:
smallPs = [2 3 5 7 11 13 17 19 61];

if any(smallPs == n)
  isPrime = 1;
  return
end

if (n < 20)
  % Primes under 20 dealt with in previous clause
  isPrime = 0;
  return
end


if (n > 4759123141)
  warn('isPrime_MillerRabin: number exceeds maximum testable with this version of algorith');
  warn('result is not definite');
end


s = 0;
d = n-1;

% Express n-1 as 2^s * d with d odd
while mod(d, 2) == 0
  s = s + 1;
  d = d / 2;
end

if s == 0
  % n-1 must be even for prime n,  so s >= 1 must hold.
  isPrime = 0;
  return
end

a = [2 7 61];

isPrime = 1;

for i = 1:3
  
  aa = pow_a_b_mod_n(a(i), d, n);
    
  isComposite = (aa ~= 1) && (aa ~= n-1);
  
  if ~isComposite
    continue;
  end
  
  for r = 1:(s-1)
    isComposite = isComposite && ...
      ( pow_a_b_mod_n(a(i), d*(2^r), n) ~= n-1 );
  end
  
  if isComposite
    isPrime = 0;
    return
  end
  
end

return

function testing

isPrime_MillerRabin(7937)
return

K = 20;
ps = zeros(1, K);
n = 11;
a = 7;
for i = 1:K
  ps(i) = pow_a_b_mod_n( a, i, n);
end

disp(ps)

N = 200;
isP = zeros(1, N);

for i = 1:N
  if isPrime_MillerRabin(i)
    isP(i) = 1;
  end
end

disp( [N-10:N ; isP(N-10:N)] )

fst = 214748293;
last = 214748295;
fst=7918; last=7952;
for i = fst:last
  if isPrime_MillerRabin(i)
    disp(i)
  end
end


return


