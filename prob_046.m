% 
% It was proposed by Christian Goldbach that every odd composite number can
% be written as the sum of a prime and twice a square.
% 
% 9  =  7 + 2×1^2 
% 15 =  7 + 2×2^2 
% 21 =  3 + 2×3^2 
% 25 =  7 + 2×3^2 
% 27 = 19 + 2×2^2 
% 33 = 31 + 2×1^2
% 
% It turns out that the conjecture was false.
% 
% What is the smallest odd composite that cannot be written as the sum of a
% prime and twice a square?

% A: 5777


function prob_046

fid = fopen('firstMillionPrimes.txt');
data = textscan(fid, '%u');
plist = single(data{1});

pMax = plist(end);

oddVal = 7;

while oddVal < pMax
  oddVal = oddVal + 2;
  
  if find(plist == oddVal, 1, 'first')
    continue;
  end
  
  ps = plist(plist < oddVal);
  temp = sqrt(0.5 * (-1 * ps + oddVal));
  temp = abs(temp - round(temp));
  if any(temp < eps)
    continue;
  end
  
  break
  
end

disp(oddVal);

return
