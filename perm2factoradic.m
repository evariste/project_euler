function d = perm2factoradic(p)
% Return the factoradic representation of a given permutation of n elements
% p.
%
% AKA the Lehmer code.
% http://www.mathe2.uni-bayreuth.de/frib/KERBER/h00/node30.html



% How many elements are we dealing with?
n = numel(p);

if any (1:n ~= sort(unique(p)))
  error('perm2factoradic: p Must have distinct elements 1 .. n');
end

d = zeros(1, n);

for i=1:n-1
  d(i) = numel(find(  p(i) > p(i+1:end)  ));
end


return
