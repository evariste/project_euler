function val = pow_a_b_mod_n(a, index, n)
% val = mod(a^b, n)

n = uint64(n);

% Successive powers of a will be cyclic mod n , what is the period of the
% cycle?


if index < n
  % Easy case:
  
  % The binary representation of the index can be used.
  % a^index can be expressed as a product of a subset of elements chosen from
  % a^1 a^2 a^4 a^8 ...
  % The subset corresponds to the ones in the binary representation of index

  val = 1;
  a = mod(a, n);
  while (index > 0) && (val > 0)
    m = mod(index, 2);
    if m > 0
      val = mod(val * a, n);
    end
    
    a = mod( a*a, n);
    index = (index - m) / 2;
  end
  
  
  return
end

% Harder case.
% Index is large:

storedPowers = zeros(2*n, 1);

storedPowers(1) = mod(a, n);

i = 2;
cycleFound = false;

while (i < 2*n) && (~cycleFound)
  curr = mod(storedPowers(i-1) * a, n);
  storedPowers(i) = curr;
  start = find(storedPowers(1:i-1) == curr, 1, 'first');
  if any(start)
    cycleFound = true;
    cycleLength = i - start;
  end
  i = i + 1;
end

if (i == 2*n) && (~cycleFound)
  error('pow_a_b_mod_n : no cycle found');
end


ind = start + mod(index - start, cycleLength);

val = storedPowers(ind);

return
