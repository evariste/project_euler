function p = factoradic2perm(digits)
% Convert a factoradic number into a permutation of n elements where n is
% the size of the vector 'digits' being passed.
%
% Permutation is assumed to be of the n element set {1, .., n}
%
% See Lehmer code:
% http://www.mathe2.uni-bayreuth.de/frib/KERBER/h00/node30.html


n = numel(digits);


vals = 1:n;

p = zeros(1,n);

for i = 1:n-1
  d = digits(i);
  p(i) = vals(1 + d);
  vals = [vals(1:d) vals(d+2:end)];
end

p(end) = vals(1);

return
