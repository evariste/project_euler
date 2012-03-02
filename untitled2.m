function isPrime = untitled2(n)

s = 0;
d = n;

while mod(d, 2) == 0
  s = s + 1;
  d = d / 2;
end

a = [2 7 61];

isPrime = 1;

i = 1;

while isPrime && i < 3
  
  val = true;
  
  aa = pow_a_b_mod_n(a(i), d, n);
  val = val && (aa ~= 1) && (aa ~= -1);

  
  for r = 1:(s-1)
    val = val && (pow_a_b_mod_n(a(i), d*(2^r), n) ~= n-1);
  end
  
  if val
    isPrime = 0;
    return
  end
  
  i = i + 1;
end

return

clear
close all


fid = fopen('firstMillionPrimes.txt');
data = textscan(fid, '%u');
data = data{1};

nMax = 10000;

primeCount = zeros(nMax, 1);

pApprox = primeCount;

for i = 2:numel(data)
  if data(i)-1 > nMax
    primeCount(data(i-1):end) = i-1;
    break;
  else
    primeCount(data(i-1):data(i)-1) = i-1;
  end
  
end

for i = 2:numel(pApprox)
  pApprox(i) = pApprox(i-1) + (1 / log(i+0.5));
end
primeCount(end) = primeCount(end-1);

plot(primeCount)

x = 1:nMax;
p = x ./ log(x);
hold on
plot(p, 'r:')

plot(pApprox, 'k:')




return


