function prob_053

% There are exactly ten ways of selecting three from five, 12345:
% 
% 123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
% 
% In combinatorics, we use the notation, 5C3 = 10.
% 
% In general,
%
%          n!
% nCr = --------
%       r!(n?r)!
%
% where r ? n, n! = n×(n?1)×...×3×2×1, and 0! = 1.
% 
% It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.
% 
% How many, not necessarily distinct, values of  nCr, for 1 ? n ? 100, 
% are greater than one-million?

% Solution: 4075

% The diagonals in this matrix give the rows of pascal's triangle
a = pascal(101);

% The diagonal starting at bottom left going up to top right gives the
% entries for 100 choose k for k = 0,1,...,100.

% Need to reject all values below this diagonal.
aa = fliplr(a);
aa = triu(aa);
aa = fliplr(aa);

% Reject all values less than or equal to a million
aa (aa<=1e06) = 0;
% Keep all values above.
aa(aa>1e06) = 1;

imagesc(aa)

% Count
numel(aa(aa>0))

return
