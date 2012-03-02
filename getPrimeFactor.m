%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
function pFac = getPrimeFactor(n)
% Return the smallest prime factor we can find for n

maxVal = 1 + floor(sqrt(n));

% In case n is prime
pFac = n;
pList = 2;

while pList(end) < maxVal
  if mod(n, pList(end)) == 0
    pFac = pList(end);
    break;
  end
  pList = growPrimeList(pList);
end

return
