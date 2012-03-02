% A permutation is an ordered arrangement of objects. For example, 3124 is
% one possible permutation of the digits 1, 2, 3 and 4. If all of the
% permutations are listed numerically or alphabetically, we call it
% lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
% 
% 012   021   102   120   201   210
% 
% What is the millionth lexicographic permutation of the digits 0, 1, 2, 3,
% 4, 5, 6, 7, 8 and 9?

% A : 2783915460


function prob_024

noOfElts = 10;
permRequired  = 1e06;
indexRequired = permRequired - 1;

digits = decimal2factoradic(indexRequired, noOfElts);

% Problem used zero indexing for the elemnts.
p = factoradic2perm(digits) - 1;

strrep(num2str(p), ' ', '')

% More playing.
n = 4;

for x = 0:23
  digits = decimal2factoradic(x, n);

  p = factoradic2perm(digits);
  
  disp([x digits p]);
  
end

return




