% We shall say that an n-digit number is pandigital if it makes use of all
% the digits 1 to n exactly once; for example, the 5-digit number, 15234,
% is 1 through 5 pandigital.
% 
% The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
% multiplicand, multiplier, and product is 1 through 9 pandigital.
% 
% Find the sum of all products whose multiplicand/multiplier/product
% identity can be written as a 1 through 9 pandigital.
% 
% HINT: Some products can be obtained in more than one way so be sure to
% only include it once in your sum.
% 
%
%
% A: 45228

function prob_032

% m-digit number x n-digit number :
% Min value 10^(m-1) * 10^(n-1) = 10^(m+n-1-1) -> m+n-1 digits
% Max value (10^m - 1)*(10^n - 1) = 10^(m+n) - 10^m - 10^n + 1 -> m+n
% digits

% So the possibilites for the number of digits in a product are 
%
% m, n and m+n-1    or   m, n and m+n
%
% if all the digits from 1 to 9 are used then either
%
% 2m+2n-1 = 9 or 2m+2n = 9, i.e. either
% m+n = 5     or 2m+2n=9
%
% m,n are whole so second solution not possible.
% So choices for m,n w.l.o.g are 1,4 and 2,3
%
% So choices for the no. of digits in a product a x b = c with a,b,c being
% pandigital when combined are 1,4,4 and 2,3,4
%

clear
close all

digs = 1:9;

allProds = [];

for m = 1:2;

  n = 5 - m;
  nProdDigits = m + n - 1;

  
  dec4fst = ones(m, 1);
  for i = 2:numel(dec4fst)
    dec4fst(i) = 10 * dec4fst(i-1);
  end
  dec4fst = flipud(dec4fst);
  
  dec4prod = ones(nProdDigits, 1);
  for i = 2:numel(dec4prod)
    dec4prod(i) = 10 * dec4prod(i-1);
  end
  dec4prod = flipud(dec4prod);
  
  
  perms4fst = npermk(digs, m);
  
  
  
  for i = 1:size(perms4fst,1)
    fst = perms4fst(i,:) * dec4fst;
    remaining = setdiff(digs, perms4fst(i,:));

    % Doh need permutations ..
    perms4prod = npermk(remaining, nProdDigits);
        
    prods = perms4prod * dec4prod;
    nProds = numel(prods);
    
    lo = 10^(n-1);
    hi = 10^(n) - 1;
    
    for j = 1:nProds
      
      snd = prods(j) / fst;
      if snd ~= round(snd)
        continue;
      end
      
      % fst does divide product.
      if snd < lo || snd > hi
        continue;
      end
      
      currDigs = union(num2str(fst), num2str(prods(j)));
      currDigs = union(currDigs, num2str(snd));
      
      
      if length(currDigs) < 9 || any(findstr(currDigs, '0'))
        continue
      end
      
%       disp([fst snd fst*snd prods(j)]);
      fprintf('%d x %d = %d\n', fst, snd, prods(j));
      allProds = [allProds; prods(j)];
      
    end
    
    
    
  end

end

disp(sum(unique(allProds)))


return


