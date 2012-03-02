% Starting in the top left corner of a 2×2 grid, there are 6 routes
% (without backtracking) to the bottom right corner.
% 
% How many routes are there through a 20×20 grid?

% Ans: 137846528820


size = 2;

nchoosek(2 * size, size)

size = 20;

sym( nchoosek(2 * size, size) )
