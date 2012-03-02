function val = pow_a_b_mod_n(a, b, n)
% val = mod(a^b, n)

% Successive powers of a will be cyclic mod n , what is the period of the
% cycle?


if b < n
  % Easy case:
  val = mod(a, n);
  
  while val > 0 && b > 1
    val = mod(val * a, n);
    b = b - 1;
  end
  return
end

% Harder case.
% Index is large:

storedPowers = zeros(n - 1, 1);

storedPowers(1) = mod(a, n);

for i = 2:n-1
  storedPowers(i) = mod(a * storedPowers(i-1), n);
end

% Find the first cycle of powers

startCycle = 1;

foundEnd = false;

while ~foundEnd && startCycle < n-2
  cycleLength = find(storedPowers(1+startCycle:end) == storedPowers(startCycle), 1, 'first');
  if any(cycleLength)
    foundEnd = true;
  else
    startCycle = startCycle + 1;
  end
end

ind = b - startCycle + 1;
ind = startCycle + 1 + mod(ind, cycleLength);

val = storedPowers(ind);

return
