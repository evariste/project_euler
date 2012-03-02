function permutations = npermk(v, k)
% Return all permutations of k elements chosen from array  v.

combs  = nchoosek(v, k);

permKInds = perms(1:k);
nPermKInds = size(permKInds, 1);

permutations = repmat(combs, nPermKInds, 1);

nCombs = size(combs, 1);

r = 1;
for i = 1:nPermKInds
  permutations(r:r+nCombs-1, :) = combs(:, permKInds(i,:));
  r = r + nCombs;
end

return
