function prob_018

% By starting at the top of the triangle below and moving to adjacent
% numbers on the row below, the maximum total from top to bottom is 23.
% 
% 3
% 7 4
% 2 4 6
% 8 5 9 3
% 
% That is, 3 + 7 + 4 + 9 = 23.
% 
% Find the maximum total from top to bottom of the triangle below:
% 
% 75
% 95 64
% 17 47 82
% 18 35 87 10
% 20 04 82 47 65
% 19 01 23 75 03 34
% 88 02 77 73 07 63 67
% 99 65 04 28 06 16 70 92
% 41 41 26 56 83 40 80 70 33
% 41 48 72 33 47 32 37 16 94 29
% 53 71 44 65 25 43 91 52 97 51 14
% 70 11 33 28 77 73 17 78 39 68 17 57
% 91 71 52 38 17 14 91 43 58 50 27 29 48
% 63 66 04 68 89 53 67 30 73 16 69 87 40 31
% 04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
% 
% NOTE: As there are only 16384 routes, it is possible to solve this
% problem by trying every route. However, Problem 67, is the same challenge
% with a triangle containing one-hundred rows; it cannot be solved by brute
% force, and requires a clever method! ;o)

% A: 1074 for problem 18.
% 7273 for problem 67

clear;
close all;

file = 'prob_018.data';
file = 'prob_067.data';

fid = fopen(file);
data = textscan(fid, '%u');
data = data{1};

rows = floor(sqrt(2*numel(data)));

if numel(data) ~= 0.5 * rows * (rows+1)
  error('We expect the number of data items to form a triangle number.');
end

m = zeros(rows, rows);
count = 1;
for i = 1:rows
  for j = 1:i
    m(i,j) = data(count);
    count = count+1;
  end
end

mStore = m;

tic
while rows > 1
  m = processRow(m);
  rows = size(m,1);
end
fprintf('%d\n', m);
toc


% 
m = mStore;

tic
fprintf('%d\n', getMaxTotal(m));
toc % 
% about 200 times slower than earlier method on the small problem.
% Unfeasibly slow on the large problem (67)


return

% A recursive version which should be slower.
function maxTotal = getMaxTotal(mIn)

% root node is at 1,1

if size(mIn,1) == 1
  maxTotal = mIn(1,1);
  return
end

left  = mIn(2:end, 1:end-1);
right = mIn(2:end, 2:end);

maxTotal = mIn(1,1) + max( getMaxTotal(left) , getMaxTotal(right) );

return


% A non-recursive (iterative) 'bottom up' method which should be quick and
% scalable.
function mOut = processRow (mIn)
%
% Loop over the entries in the bottom row of the tree (mIn) in pairs. Work
% out the best to incorporate with the level above with the aim of finding
% the best sum over all paths in the tree. A three level example.
% 
% a
% |\
% b c
% |\|\
% d e f
% 
% is changed to matrix
% 
% a
% |\
% g h
% 
% where g = b + max(d,e) and h = c + max(e,f)

% mIn should be square and all entries above the diagonal are assumed to be
% zero and ignored. Tree is represented by entries on diagonal and below.

[r, c] = size(mIn);
if r ~= c
  error('Matrix must be square.');
end

if r == 1
  mOut = mIn;
  return
end

for j = 1:c-1
  mIn(r-1, j) = mIn(r-1, j) + max(mIn(r, j:j+1));
end

mOut = mIn(1:r-1, 1:r-1);

return
