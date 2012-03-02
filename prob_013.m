% Work out the first ten digits of the sum of the following one-hundred
% 50-digit numbers.

% A: 5537376230

tic

fid = fopen('prob_013.data');
data = textscan(fid, '%s');
% Get the contents of the cell array
data = data{1};

% Convert to symbol.
datasym = sym(data);

total = sum(datasym);

totalChar = char(total);

disp( totalChar(1:10) );

toc

