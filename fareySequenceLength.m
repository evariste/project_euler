function fLen = fareySequenceLength(n)
% Number of fractions in Farey Sequence with denominators less than or
% equal to n.  INCLUDING 0/1 and 1/1 at the ends!

fLen = 0;

if n < 1
  return
end

fLen = 2;

if n == 1
  return 
end

fLen = n * (n + 3) / 2;


d = 2;

while d <= n
  floorNOverD = floor(n / d);
  dStart = d;
  while floor( n / (d+1) ) == floorNOverD && d < n
    d = d + 1;
  end
  
  fLen = fLen - (1 + d - dStart) * fareySequenceLength(floorNOverD);
  
  
  d = d + 1;
end

return