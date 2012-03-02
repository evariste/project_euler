function pInv = inversePermutation(p)
% p is an array consisting of a permutation of the digits 1 .. N
%
% pInv returned is the inverse permutation, i.e.
%
% p o pInv = pInv o p = [1, 2, .., N]

N = numel(p);

if any ( sort(p) ~= 1:N )
  error('inversePermutation: Not a valid permutation');
end

if min(size(p)) ~= 1
  error('inversePermutation: permuation must be a vector');
end

if numel(size(p)) > 2
  error('inversePermutation: permutation has incorrect dimension');
end


pInv = zeros(size(p));
pInv(p) = 1:N;

return

