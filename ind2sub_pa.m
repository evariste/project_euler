function subs = ind2sub_pa(dims, i)
% Convert a linear index i into a set of subscripts based on the values
% given in dims.
%
% Matlab style 1-indexing
%
if min(size(dims)) > 1 || numel(size(dims)) ~= 2
  error('ind2sub_pa : dimensions not appropriate');
end

if size(dims, 2) == 1
  dims = dims.';
end


cycleLengths = [1 cumprod(dims)];
subs = zeros(1, length(dims));

for j = 1:length(dims)
  subs(j) = 1 + mod( floor( (i-1) / cycleLengths(j) ) , dims(j) );
end

return
